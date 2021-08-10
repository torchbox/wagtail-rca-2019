# Generated by Django 3.1.10 on 2021-08-05 11:53

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0006_adds_key_details_field"),
        ("images", "0003_extends_image_fields"),
        ("events", "0009_event_booking_20210728_1339"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventindexpage", options={"verbose_name": "Event Listing Page"},
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_email",
            field=models.EmailField(
                blank=True, max_length=254, verbose_name="Contact email"
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_form",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="forms.formpage",
                verbose_name="Contact form",
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.customimage",
                verbose_name="Contact image",
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_link_text",
            field=models.CharField(
                blank=True,
                help_text="Optional text for the linked url, form or email",
                max_length=120,
                verbose_name="Contact link text",
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_text",
            field=models.CharField(
                blank=True,
                help_text="Maximum length of 250 characters",
                max_length=250,
                verbose_name="Contact text",
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_title",
            field=models.CharField(
                blank=True,
                help_text="Maximum length of 120 characters",
                max_length=120,
                verbose_name="Contact title",
            ),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="contact_model_url",
            field=models.URLField(blank=True, verbose_name="Contact url"),
        ),
        migrations.AddField(
            model_name="eventindexpage",
            name="introduction",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name="EventIndexPageRelatedEditorialPage",
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
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="events.eventdetailpage",
                    ),
                ),
                (
                    "source_page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_event_pages",
                        to="events.eventindexpage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
    ]
