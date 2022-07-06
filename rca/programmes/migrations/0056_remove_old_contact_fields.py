# Generated by Django 2.2.12 on 2021-01-05 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("utils", "0019_update_contact_fields"),
        ("programmes", "0055_add_new_contact_fields"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programmeindexpage",
            name="contact_email",
        ),
        migrations.RemoveField(
            model_name="programmeindexpage",
            name="contact_image",
        ),
        migrations.RemoveField(
            model_name="programmeindexpage",
            name="contact_text",
        ),
        migrations.RemoveField(
            model_name="programmeindexpage",
            name="contact_title",
        ),
        migrations.RemoveField(
            model_name="programmeindexpage",
            name="contact_url",
        ),
        migrations.RemoveField(
            model_name="programmepage",
            name="contact_email",
        ),
        migrations.RemoveField(
            model_name="programmepage",
            name="contact_image",
        ),
        migrations.RemoveField(
            model_name="programmepage",
            name="contact_url",
        ),
    ]
