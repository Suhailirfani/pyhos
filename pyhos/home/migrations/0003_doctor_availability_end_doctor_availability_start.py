# Generated by Django 5.0 on 2024-06-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_patient_address_patient_dob_patient_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='availability_end',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='availability_start',
            field=models.TimeField(null=True),
        ),
    ]
