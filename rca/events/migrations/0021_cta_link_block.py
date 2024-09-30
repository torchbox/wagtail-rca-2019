# Generated by Django 4.2.11 on 2024-09-19 10:54

from django.db import migrations
import rca.navigation.models
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0020_eventdetailpage_location_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventdetailpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            form_classname="full title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading_block.html",
                        ),
                    ),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(
                                        form_classname="title",
                                        help_text="Enter quote text only, there is no need to add quotation marks",
                                    ),
                                ),
                                ("author", wagtail.blocks.CharBlock(required=False)),
                                ("job_title", wagtail.blocks.CharBlock(required=False)),
                            ]
                        ),
                    ),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "jw_video",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Optional title to identify the video. Not shown on the page.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "video_url",
                                    wagtail.blocks.URLBlock(
                                        help_text="The URL of the video to show.",
                                        max_length=1000,
                                    ),
                                ),
                                (
                                    "poster_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="The poster image to show as a placeholder for the video. For best results use an image 1920x1080 pixels"
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "cta_link",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "url",
                                    rca.navigation.models.URLOrRelativeURLBLock(
                                        required=False
                                    ),
                                ),
                                (
                                    "page",
                                    wagtail.blocks.PageChooserBlock(required=False),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Leave blank to use the page's own title, required if using a URL",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
