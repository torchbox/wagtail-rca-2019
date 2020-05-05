# Generated by Django 2.2.12 on 2020-05-02 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("landingpages", "0010_add_max_length_to_help_texts"),
    ]

    operations = [
        migrations.RemoveField(model_name="landingpagestatsblock", name="link_text"),
        migrations.RemoveField(model_name="landingpagestatsblock", name="link_url"),
        migrations.AddField(
            model_name="landingpagestatsblock",
            name="page_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
    ]
