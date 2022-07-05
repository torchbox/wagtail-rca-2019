# Generated by Django 2.2.12 on 2021-01-20 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0013_add_related_staff_fields"),
    ]

    operations = [
        migrations.RenameField(
            model_name="schoolpage",
            old_name="next_open_day_end_date",
            new_name="next_open_day_date",
        ),
        migrations.RemoveField(
            model_name="schoolpage",
            name="next_open_day_start_date",
        ),
    ]
