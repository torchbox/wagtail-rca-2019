# Generated by Django 2.2.12 on 2021-03-09 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("enquire_to_study", "0003_enquiry_submission"),
    ]

    operations = [
        migrations.CreateModel(
            name="EnquireToStudySettings",
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
                    "email_submission_notifations",
                    models.BooleanField(
                        default=True,
                        help_text="When checked, submission confirmation email notifications will be sent to the user who filled out the form",
                    ),
                ),
                ("email_subject", models.CharField(max_length=255)),
                ("email_content", models.TextField()),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Enquire to study settings",
            },
        ),
    ]
