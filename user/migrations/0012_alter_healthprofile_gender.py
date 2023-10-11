# Generated by Django 4.2.5 on 2023-10-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_healthprofile_blood_glucose_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True),
        ),
    ]