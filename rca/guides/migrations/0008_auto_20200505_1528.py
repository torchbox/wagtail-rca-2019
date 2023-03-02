# Generated by Django 2.2.12 on 2020-05-05 14:28

import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("guides", "0007_merge_20200505_1521")]

    operations = [
        migrations.AlterField(
            model_name="guidepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "anchor_heading",
                        wagtail.blocks.CharBlock(
                            classname="full title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/anchor_heading_block.html",
                        ),
                    ),
                    (
                        "heading",
                        wagtail.blocks.CharBlock(
                            classname="full title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading_block.html",
                        ),
                    ),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "caption",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(
                                        classname="title",
                                        help_text="Enter quote text only, there is no need to add quotation marks",
                                    ),
                                ),
                                (
                                    "author",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "job_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ]
                        ),
                    ),
                    ("embed", wagtail.embeds.blocks.EmbedBlock()),
                ]
            ),
        )
    ]
