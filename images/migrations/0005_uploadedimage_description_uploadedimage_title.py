# Generated by Django 5.1.7 on 2025-03-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_remove_uploadedimage_title_uploadedimage_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
