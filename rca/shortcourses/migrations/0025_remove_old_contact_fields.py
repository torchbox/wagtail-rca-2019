# Generated by Django 2.2.12 on 2021-01-05 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortcourses", "0024_add_new_contact_fields"),
        ("utils", "0019_update_contact_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shortcoursepage",
            name="contact_email",
        ),
        migrations.RemoveField(
            model_name="shortcoursepage",
            name="contact_image",
        ),
        migrations.RemoveField(
            model_name="shortcoursepage",
            name="contact_text",
        ),
        migrations.RemoveField(
            model_name="shortcoursepage",
            name="contact_url",
        ),
    ]
