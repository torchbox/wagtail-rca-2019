# Generated by Django 3.1.10 on 2021-07-16 09:23

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("images", "0003_extends_image_fields"),
        ("editorial", "0003_add_contact_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="EditorialListingPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("social_text", models.CharField(blank=True, max_length=255)),
                (
                    "listing_title",
                    models.CharField(
                        blank=True,
                        help_text="Override the page title used when this page appears in listings",
                        max_length=255,
                    ),
                ),
                (
                    "listing_summary",
                    models.CharField(
                        blank=True,
                        help_text="The text summary used when this page appears in listings. It's also used as the description for search engines if the 'Search description' field above is not defined.",
                        max_length=255,
                    ),
                ),
                ("introduction", models.CharField(blank=True, max_length=200)),
                (
                    "listing_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Choose the image you wish to be displayed when this page appears in listings",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.customimage",
                    ),
                ),
                (
                    "social_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.customimage",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page", models.Model),
        ),
        migrations.CreateModel(
            name="EditorialListingRelatedEditorialPage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "page",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="editorial.editorialpage",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_editorial_pages",
                        to="editorial.editoriallistingpage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
    ]
