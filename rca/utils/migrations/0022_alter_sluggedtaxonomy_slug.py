# Generated by Django 3.2.11 on 2022-01-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0021_tap_widget_carousel_settings"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sluggedtaxonomy",
            name="slug",
            field=models.SlugField(blank=True, max_length=128),
        ),
    ]
