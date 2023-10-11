# Generated by Django 4.2.5 on 2023-09-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_healthprofile_bmi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprofile',
            name='bmi',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Body Mass Index', max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='healthprofile',
            name='calories',
            field=models.FloatField(blank=True, help_text='Daily calorie requirements', null=True),
        ),
        migrations.AlterField(
            model_name='healthprofile',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='healthprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture/'),
        ),
    ]