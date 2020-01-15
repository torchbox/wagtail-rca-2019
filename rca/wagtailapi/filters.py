from django.conf import settings
from rest_framework import filters
from wagtail.api.v2.utils import BadRequestError
from wagtail.search.backends import get_search_backend
from wagtail.search.backends.base import FilterFieldError, OrderByFieldError

from rca.programmes.models import ProgrammePageRelatedSchoolsAndResearchPage
from rca.schools.models import SchoolsAndResearchPage


class DegreeLevelFilter(filters.BaseFilterBackend):
    """
    Allows to filter pages by one or multiple projects
    """

    def filter_queryset(self, request, queryset, view):
        pks = request.GET.getlist("project", [])

        if pks:
            queryset = queryset.filter(degree_level__in=pks)

        return queryset


class SubjectsFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if hasattr(queryset.model, "subjects"):
            subject_ids = request.GET.getlist("subjects", [])
            if subject_ids:
                queryset = queryset.model.objects.filter(
                    subjects__subject__in=subject_ids
                )

        return queryset


class RelatedSchoolsFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if hasattr(queryset.model, "related_schools_and_research_pages"):
            school_ids = request.GET.getlist("related_schools_and_research_pages", [])
            if school_ids:
                school_pages = (
                    SchoolsAndResearchPage.objects.all()
                    .live()
                    .filter(id__in=school_ids)
                )
                programme_pages_with_school_pages_relationship = (
                    ProgrammePageRelatedSchoolsAndResearchPage.objects.all()
                )
                relationship_objects = programme_pages_with_school_pages_relationship.filter(
                    page__in=school_pages
                ).values_list(
                    "id", flat=True
                )

                queryset = queryset.model.objects.filter(
                    related_schools_and_research_pages__id__in=relationship_objects
                )
        return queryset


class SearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        """
        This overrides the wagtail core api filters.SearchFilter
        so we can provide autocomplet/fuzzy text matching with
        sb.autocomplete
        """
        search_enabled = getattr(settings, "WAGTAILAPI_SEARCH_ENABLED", True)

        if "search" in request.GET:
            if not search_enabled:
                raise BadRequestError("search is disabled")

            # Searching and filtering by tag at the same time is not supported
            if getattr(queryset, "_filtered_by_tag", False):
                raise BadRequestError(
                    "filtering by tag with a search query is not supported"
                )

            search_query = request.GET["search"]
            search_operator = request.GET.get("search_operator", None)
            order_by_relevance = "order" not in request.GET

            sb = get_search_backend()
            try:
                queryset = sb.autocomplete(
                    search_query,
                    queryset,
                    operator=search_operator,
                    order_by_relevance=order_by_relevance,
                )
            except FilterFieldError as e:
                raise BadRequestError(
                    "cannot filter by '{}' while searching (field is not indexed)".format(
                        e.field_name
                    )
                )
            except OrderByFieldError as e:
                raise BadRequestError(
                    "cannot order by '{}' while searching (field is not indexed)".format(
                        e.field_name
                    )
                )

        return queryset
