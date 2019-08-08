# Generated by Django 2.2.3 on 2019-08-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("utils", "0002_add_extra_social_settings")]

    operations = [
        migrations.AddField(
            model_name="socialmediasettings",
            name="facebook_page_name",
            field=models.CharField(
                blank=True,
                help_text="Your Facebook Page URL e.g. torchbox",
                max_length=255,
            ),
        )
    ]
