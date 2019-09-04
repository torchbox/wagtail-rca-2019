# Generated by Django 2.2.4 on 2019-09-04 15:45

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0019_increase_character_limits")]

    operations = [
        migrations.AddField(
            model_name="programmetype",
            name="legacy_slug",
            field=models.CharField(
                blank=True,
                help_text="This field should match the value added as a slug in the current live RCA sites 'Programme' taxonomy, it's used for relating content like news and events.",
                max_length=128,
            ),
        ),
        migrations.AlterField(
            model_name="programmepageprogrammetype",
            name="page",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="programme_type",
                to="programmes.ProgrammePage",
            ),
        ),
    ]
