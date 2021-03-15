# Generated by Django 2.2.12 on 2021-02-18 07:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import modelcluster.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0055_stop_allowing_blank_pages"),
        ("enquire_to_study", "0002_alter_meta_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="EnquiryFormSubmission",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "country_of_residence",
                    django_countries.fields.CountryField(max_length=2),
                ),
                ("city", models.CharField(max_length=255)),
                ("is_citizen", models.BooleanField()),
                ("is_read_data_protection_policy", models.BooleanField()),
                ("is_notification_opt_in", models.BooleanField()),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="EnquiryFormSubmissionFundingsOrderable",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "enquiry_submission",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enquiry_submission_funding",
                        to="enquire_to_study.EnquiryFormSubmission",
                    ),
                ),
                (
                    "funding",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enquire_to_study.Funding",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="EnquiryFormSubmissionProgrammesOrderable",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "enquiry_submission",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enquiry_submission_programmes",
                        to="enquire_to_study.EnquiryFormSubmission",
                    ),
                ),
                (
                    "programme",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="programmes.ProgrammePage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="EnquiryFormSubmissionProgrammeTypesOrderable",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "enquiry_submission",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="enquiry_submission_programme_types",
                        to="enquire_to_study.EnquiryFormSubmission",
                    ),
                ),
                (
                    "programme_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="programmes.ProgrammeType",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.RenameModel(old_name="InquiryReason", new_name="EnquiryReason",),
        migrations.RemoveField(
            model_name="submissionfundingsorderable", name="funding",
        ),
        migrations.RemoveField(
            model_name="submissionfundingsorderable", name="submission",
        ),
        migrations.DeleteModel(name="Submission",),
        migrations.DeleteModel(name="SubmissionFundingsOrderable",),
        migrations.AddField(
            model_name="enquiryformsubmission",
            name="enquiry_reason",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="enquire_to_study.EnquiryReason",
            ),
        ),
        migrations.AddField(
            model_name="enquiryformsubmission",
            name="start_date",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="enquire_to_study.StartDate",
            ),
        ),
    ]
