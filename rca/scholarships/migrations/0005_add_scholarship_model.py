# Generated by Django 3.1.14 on 2021-12-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0066_add_intranet_slug_for_imports"),
        ("scholarships", "0004_adds_form_configuration_fields"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="scholarshipfeestatus",
            options={
                "ordering": ("title",),
                "verbose_name_plural": "Scholarship Fee Statuses",
            },
        ),
        migrations.AlterModelOptions(
            name="scholarshipfunding",
            options={"ordering": ("title",)},
        ),
        migrations.AlterModelOptions(
            name="scholarshiplocation",
            options={"ordering": ("title",)},
        ),
        migrations.CreateModel(
            name="Scholarship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("active", models.BooleanField(default=True)),
                ("summary", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=100)),
                (
                    "eligable_programmes",
                    models.ManyToManyField(to="programmes.ProgrammePage"),
                ),
                (
                    "fee_statuses",
                    models.ManyToManyField(to="scholarships.ScholarshipFeeStatus"),
                ),
                (
                    "funding_categories",
                    models.ManyToManyField(to="scholarships.ScholarshipFunding"),
                ),
            ],
        ),
    ]
