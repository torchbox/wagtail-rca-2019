# Generated by Django 2.2.9 on 2020-04-07 10:09

import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0001_initial"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("images", "0002_customimage_file_hash"),
        ("programmes", "0051_update_revisions"),
        ("shortcourses", "0006_add_short_course_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="shortcoursepage",
            name="contact_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="contact_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="contact_text",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="contact_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="external_links",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "link",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                ("url", wagtail.core.blocks.URLBlock(required=False)),
                            ]
                        ),
                    )
                ],
                blank=True,
                verbose_name="External Links",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="gallery",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "slide",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "author",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                ("link", wagtail.core.blocks.URLBlock(required=False)),
                                (
                                    "course",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                verbose_name="Gallery",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="location",
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="programme_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="programmes.ProgrammeType",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="quote_carousel",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "quote",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.core.blocks.CharBlock(classname="title"),
                                ),
                                (
                                    "author",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "job_title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                verbose_name="Quote carousel",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="show_register_link",
            field=models.BooleanField(
                default=1,
                help_text="If selected, a 'Register your interest' link will be                                                                    visible in the key details section",
            ),
        ),
        migrations.AddField(
            model_name="shortcoursepage",
            name="staff_title",
            field=models.CharField(
                blank=True,
                help_text="Heading to display above the short course team members, E.G Programme Team",
                max_length=50,
            ),
        ),
        migrations.CreateModel(
            name="ShortCourseRelatedStaff",
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
                ("name", models.CharField(max_length=125)),
                ("role", models.CharField(blank=True, max_length=125)),
                ("description", models.TextField(blank=True)),
                ("link", models.URLField(blank=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.CustomImage",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="people.StaffPage",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_staff",
                        to="shortcourses.ShortCoursePage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="ShortCoursePageRelatedProgramme",
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
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_programmes",
                        to="shortcourses.ShortCoursePage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="FeeItem",
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
                ("text", models.CharField(max_length=128)),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fee_items",
                        to="shortcourses.ShortCoursePage",
                    ),
                ),
            ],
        ),
    ]
