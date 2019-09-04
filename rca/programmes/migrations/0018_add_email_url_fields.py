# Generated by Django 2.2.4 on 2019-09-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0017_introduction_should_not_be_required")]

    operations = [
        migrations.AddField(
            model_name="programmepage",
            name="contact_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="programmepage",
            name="contact_url",
            field=models.URLField(blank=True),
        ),
    ]
