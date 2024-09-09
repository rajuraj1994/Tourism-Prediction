# Generated by Django 3.2.5 on 2022-01-27 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='day_one',
            new_name='place_desc',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='dest_image',
            new_name='place_image',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='dest_location',
            new_name='place_location',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='dest_name',
            new_name='place_name',
        ),
        migrations.RemoveField(
            model_name='place',
            name='day_three',
        ),
        migrations.RemoveField(
            model_name='place',
            name='day_two',
        ),
        migrations.RemoveField(
            model_name='place',
            name='dest_desc',
        ),
        migrations.RemoveField(
            model_name='place',
            name='dest_price',
        ),
        migrations.RemoveField(
            model_name='place',
            name='dest_type',
        ),
        migrations.RemoveField(
            model_name='place',
            name='total_person',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
