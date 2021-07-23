# Generated by Django 3.1.10 on 2021-07-23 15:07

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0003_extends_image_fields"),
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("events", "0005_event_eligibility_20210722_1412"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventdetailpage",
            name="speaker_heading",
            field=models.CharField(blank=True, max_length=120, verbose_name="Heading"),
        ),
        migrations.CreateModel(
            name="EventDetailPageSpeaker",
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
                ("first_name", models.CharField(blank=True, max_length=125)),
                ("surname", models.CharField(blank=-1, max_length=125)),
                ("role", models.CharField(blank=True, max_length=125)),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="Not displayed for small teaser profiles"
                    ),
                ),
                ("link", models.URLField(blank=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.customimage",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
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
                        related_name="speakers",
                        to="events.eventdetailpage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
    ]
