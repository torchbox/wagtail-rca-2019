# Generated by Django 2.2.12 on 2020-05-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("landingpages", "0009_update_to_allow_blank")]

    operations = [
        migrations.AlterField(
            model_name="homepageslideshowblock",
            name="summary",
            field=models.CharField(
                blank=True, help_text="Maximum length of 250 characters", max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="homepageslideshowblock",
            name="title",
            field=models.CharField(
                help_text="Maximum length of 125 characters", max_length=125
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="contact_text",
            field=models.CharField(
                blank=True, help_text="Maximum length of 250 characters", max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="contact_title",
            field=models.CharField(
                blank=True, help_text="Maximum length of 120 characters", max_length=120
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="highlights_link_text",
            field=models.CharField(
                blank=True,
                help_text="The text to display for the link, maximum length of 80 characters",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="highlights_title",
            field=models.TextField(
                blank=True, help_text="Maximum length of 80 characters", max_length=80
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="introduction",
            field=models.TextField(
                blank=True, help_text="Maximum length of 500 characters", max_length=500
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="page_list_title",
            field=models.TextField(
                blank=True,
                help_text="The title to be displayed above the page list blocks, maximum length of 80 characters",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="related_pages_text",
            field=models.TextField(
                blank=True,
                help_text="The brief paragraph of text to be displayed above the related pages grid, maximum length of 80 characters",
                max_length=250,
            ),
        ),
        migrations.AlterField(
            model_name="landingpage",
            name="related_pages_title",
            field=models.TextField(
                blank=True,
                help_text="The title to be displayed above the related pages grid, maximum length of 80 characters",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimage",
            name="description",
            field=models.TextField(
                blank=True, help_text="Maximum length of 250 characters", max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimage",
            name="subtitle",
            field=models.TextField(
                blank=True, help_text="Maximum length of 120 characters", max_length=120
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimage",
            name="title",
            field=models.TextField(
                blank=True,
                help_text="The title has a maximum length of 80 characters",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimagesecondary",
            name="description",
            field=models.TextField(
                blank=True, help_text="Maximum length of 250 characters", max_length=250
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimagesecondary",
            name="subtitle",
            field=models.TextField(
                blank=True, help_text="Maximum length of 120 characters", max_length=120
            ),
        ),
        migrations.AlterField(
            model_name="landingpagefeaturedimagesecondary",
            name="title",
            field=models.TextField(
                blank=True,
                help_text="The title has a maximum length of 80 characters",
                max_length=80,
            ),
        ),
        migrations.AlterField(
            model_name="landingpagestatsblock",
            name="link_text",
            field=models.CharField(
                blank=True, help_text="Maximum length of 255 characters", max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="landingpagestatsblock",
            name="title",
            field=models.CharField(
                help_text="Maximum length of 125 characters", max_length=125
            ),
        ),
    ]
