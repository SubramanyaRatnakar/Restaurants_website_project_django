# Generated by Django 5.1.6 on 2025-02-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
    ]
