# Generated by Django 2.2.12 on 2021-03-16 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0020_swap_for_richtext_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studenttype",
            name="sluggedtaxonomy_ptr",
        ),
        migrations.DeleteModel(
            name="StudentPageStudentTypePlacement",
        ),
        migrations.DeleteModel(
            name="StudentType",
        ),
    ]
