# Generated by Django 3.2.5 on 2022-01-30 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20220128_0931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_date',
            new_name='arrival_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Denied', 'Denied')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='total_person',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
    ]
