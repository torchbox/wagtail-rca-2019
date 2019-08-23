# Generated by Django 2.2.4 on 2019-08-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0004_remove_color_option_field")]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="hero_colour_option",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Light text on dark image"),
                    (2, "dark text on light image"),
                ],
                default=1,
            ),
            preserve_default=False,
        )
    ]
