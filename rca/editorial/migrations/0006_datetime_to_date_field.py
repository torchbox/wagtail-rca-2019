# Generated by Django 3.1.10 on 2021-06-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("editorial", "0005_remove_auto_now_add"),
    ]

    operations = [
        migrations.AlterField(
            model_name="editorialpage", name="date", field=models.DateField(),
        ),
    ]
