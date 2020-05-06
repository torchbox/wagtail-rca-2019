# Generated by Django 2.2.12 on 2020-05-06 15:29

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("landingpages", "0014_add_custom_teaser_block"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="HomePageSlideshowBlock", new_name="LandingPagePageSlideshowBlock"
        ),
        migrations.AddField(
            model_name="landingpage",
            name="slideshow_summary",
            field=models.CharField(
                blank=True, help_text="Maximum length of 250 characters", max_length=250
            ),
        ),
        migrations.AddField(
            model_name="landingpage",
            name="slideshow_title",
            field=models.CharField(
                blank=True, help_text="Maximum length of 125 characters", max_length=125
            ),
        ),
        migrations.CreateModel(
            name="LandingPageRelatedPageSlide",
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
                        related_name="slideshow_page",
                        to="landingpages.LandingPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
    ]
