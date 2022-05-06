# Generated by Django 3.1.14 on 2021-12-23 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0021_tap_widget_carousel_settings"),
        ("scholarships", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScholarshipFeeStatus",
            fields=[
                (
                    "sluggedtaxonomy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="utils.sluggedtaxonomy",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Scholarship Fee Statuses",
            },
            bases=("utils.sluggedtaxonomy",),
        ),
        migrations.CreateModel(
            name="ScholarshipFunding",
            fields=[
                (
                    "sluggedtaxonomy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="utils.sluggedtaxonomy",
                    ),
                ),
            ],
            bases=("utils.sluggedtaxonomy",),
        ),
        migrations.CreateModel(
            name="ScholarshipLocation",
            fields=[
                (
                    "sluggedtaxonomy_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="utils.sluggedtaxonomy",
                    ),
                ),
            ],
            bases=("utils.sluggedtaxonomy",),
        ),
    ]
