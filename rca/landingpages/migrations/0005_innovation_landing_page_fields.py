# Generated by Django 2.2.12 on 2020-04-28 22:03

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0003_extends_image_fields"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("landingpages", "0004_landing_page_base_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="landingpage",
            name="contact_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="landingpage",
            name="contact_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
        migrations.AddField(
            model_name="landingpage",
            name="contact_text",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="landingpage",
            name="contact_title",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="landingpage",
            name="contact_url",
            field=models.URLField(blank=True, verbose_name="Contact URL"),
        ),
        migrations.CreateModel(
            name="LandingPageStatsBlock",
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
                ("title", models.CharField(max_length=125)),
                (
                    "statistics",
                    wagtail.fields.StreamField(
                        [
                            (
                                "statistic",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "summary",
                                            wagtail.blocks.CharBlock(
                                                help_text="E.g.  1 in 3 of our graduates are business owners or independent professionals",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "before",
                                            wagtail.blocks.CharBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "after",
                                            wagtail.blocks.CharBlock(
                                                help_text="E.g. '%'",
                                                max_length=2,
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "number",
                                            wagtail.blocks.IntegerBlock(
                                                help_text="E.g. '33'", required=False
                                            ),
                                        ),
                                        (
                                            "meta",
                                            wagtail.blocks.CharBlock(
                                                help_text="Small title below the number, e.g 'Nationalities'",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ]
                    ),
                ),
                ("link_url", models.URLField(blank=True)),
                ("link_text", models.CharField(blank=True, max_length=255)),
                (
                    "background_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.CustomImage",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats_block",
                        to="landingpages.LandingPage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LandingPageFeaturedImageSecondary",
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
                ("link_url", models.URLField(blank=True)),
                ("link_text", models.CharField(blank=True, max_length=255)),
                ("title", models.TextField(blank=True, max_length=80)),
                ("subtitle", models.TextField(blank=True, max_length=120)),
                ("description", models.TextField(blank=True, max_length=250)),
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
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="featured_image_secondary",
                        to="landingpages.LandingPage",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
