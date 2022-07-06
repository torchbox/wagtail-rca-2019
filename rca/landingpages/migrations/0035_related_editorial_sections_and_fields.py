# Generated by Django 3.1.10 on 2021-08-11 18:17

import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("landingpages", "0034_add_collaborators_and_cta"),
    ]

    operations = [
        migrations.AddField(
            model_name="alumnilandingpage",
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
            model_name="alumnilandingpage",
            name="latest_cta_block",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "call_to_action",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="A large heading diplayed at the top of block",
                                        required=False,
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "page",
                                    wagtail.core.blocks.PageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "title",
                                                wagtail.core.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "url",
                                                wagtail.core.blocks.URLBlock(
                                                    required=False
                                                ),
                                            ),
                                        ],
                                        help_text="An optional link to display below the expanded content",
                                        required=False,
                                    ),
                                ),
                            ],
                            label="text promo",
                        ),
                    )
                ],
                blank=True,
                verbose_name="Text promo",
            ),
        ),
        migrations.AddField(
            model_name="alumnilandingpage",
            name="latest_intro",
            field=models.CharField(
                blank=True,
                help_text="Optional short text summary for the 'Latest' section",
                max_length=250,
                verbose_name="Latest section summary",
            ),
        ),
        migrations.CreateModel(
            name="AlumniLandingPageSecondaryRelatedEditorialPage",
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
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_editorial_pages_secondary",
                        to="landingpages.alumnilandingpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AlumniLandingPageRelatedEditorialPage",
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
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_editorial_pages",
                        to="landingpages.alumnilandingpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
