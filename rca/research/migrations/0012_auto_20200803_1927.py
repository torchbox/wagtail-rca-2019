# Generated by Django 2.2.12 on 2020-08-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("research", "0011_field_label_updates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="researchcentrepagestaff",
            name="first_name",
            field=models.CharField(blank=True, max_length=125),
        ),
        migrations.AlterField(
            model_name="researchcentrepagestaff",
            name="surname",
            field=models.CharField(blank=-1, max_length=125),
        ),
    ]
