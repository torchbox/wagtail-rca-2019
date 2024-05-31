# Generated by Django 4.2.11 on 2024-05-27 07:53

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("editorial", "0026_add_sticky_cta_to_editorialpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="editorialpage",
            name="gallery",
            field=wagtail.fields.StreamField(
                [
                    (
                        "slide",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("author", wagtail.blocks.CharBlock(required=False)),
                                ("link", wagtail.blocks.URLBlock(required=False)),
                                ("course", wagtail.blocks.CharBlock(required=False)),
                                (
                                    "document",
                                    wagtail.documents.blocks.DocumentChooserBlock(
                                        help_text="Maximum file size: 10MB",
                                        required=False,
                                    ),
                                ),
                                (
                                    "video_embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="Add a YouTube or Vimeo video URL",
                                        required=False,
                                    ),
                                ),
                                (
                                    "audio_embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="Add a Soundcloud URL", required=False
                                    ),
                                ),
                                (
                                    "embed_play_button_label",
                                    wagtail.blocks.TextBlock(
                                        help_text="The label for the embed play button. If left blank, it will default to 'Play + title'.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                verbose_name="Gallery",
            ),
        ),
    ]
