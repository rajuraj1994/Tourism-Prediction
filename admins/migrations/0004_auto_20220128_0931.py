# Generated by Django 3.2.5 on 2022-01-28 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0003_alter_place_place_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='country',
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=200, null=True)),
                ('place_location', models.CharField(max_length=200, null=True)),
                ('place_desc', models.TextField(null=True)),
                ('place_image', models.FileField(null=True, upload_to='static/uploads/data')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admins.country')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.places'),
        ),
    ]
