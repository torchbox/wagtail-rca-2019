# Generated by Django 2.2.19 on 2021-04-12 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0023_add_pdf_link_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projectpage",
            name="hero_colour_option",
        ),
    ]
