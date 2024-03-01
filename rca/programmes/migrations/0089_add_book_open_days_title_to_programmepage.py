# Generated by Django 4.2.9 on 2024-02-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0088_django_40_upgrade"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programmepageglobalfieldssettings",
            name="key_details_book_or_view_all_open_days_link_title",
        ),
        migrations.AddField(
            model_name="programmepage",
            name="book_or_view_all_open_days_link_title",
            field=models.CharField(
                blank=True,
                default="Book or view all open days",
                max_length=255,
                verbose_name="Book open days title",
            ),
        ),
    ]
