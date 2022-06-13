# Generated by Django 3.1.10 on 2021-07-28 10:31

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("editorial", "0017_editorialpagerelatedprogramme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="editorialpage",
            name="introduction",
            field=wagtail.fields.RichTextField(
                blank=True, help_text="Maximum of 140 characters supported in listings"
            ),
        ),
    ]
