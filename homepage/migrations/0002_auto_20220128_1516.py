# Generated by Django 3.2.5 on 2022-01-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='preferred_call_date',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
