# Generated by Django 2.2.12 on 2021-01-20 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0014_change_to_single_open_day"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schoolpage",
            name="introduction_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
    ]
