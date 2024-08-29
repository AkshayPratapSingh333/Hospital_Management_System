# Generated by Django 5.1 on 2024-08-28 09:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Hospital", "0003_remove_doctor_doctor_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="Patient_id",
        ),
        migrations.AddField(
            model_name="patient",
            name="admission",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="patient",
            name="bill",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="patient",
            name="discharge",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="patient",
            name="docname",
            field=models.CharField(default="Unknown Doctor", max_length=100),
        ),
        migrations.AddField(
            model_name="patient",
            name="prescription",
            field=models.CharField(default="No prescription", max_length=700),
        ),
        migrations.AddField(
            model_name="patient",
            name="reason",
            field=models.CharField(default="Unknown", max_length=700),
        ),
        migrations.AlterField(
            model_name="patient",
            name="gender",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="patient",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
