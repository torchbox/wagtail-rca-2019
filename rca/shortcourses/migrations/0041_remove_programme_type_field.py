# Generated by Django 4.2.16 on 2025-01-17 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shortcourses", "0040_migrate_programme_type_to_programme_types"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shortcoursepage",
            name="programme_type",
        ),
    ]
