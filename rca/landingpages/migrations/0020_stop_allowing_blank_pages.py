# Generated by Django 2.2.12 on 2021-01-22 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landingpages", "0019_field_label_updates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="landingpagerelatedpagegrid",
            name="page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AlterField(
            model_name="landingpagerelatedpagehighlights",
            name="page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AlterField(
            model_name="landingpagerelatedpageslide",
            name="page",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
    ]
