# Generated by Django 2.2.4 on 2019-08-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("programmes", "0013_add_hero_color_option_integer")]

    operations = [
        migrations.AlterModelOptions(
            name="programmepagefeeitem", options={"ordering": ["sort_order"]}
        ),
        migrations.AddField(
            model_name="programmepagefeeitem",
            name="sort_order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
