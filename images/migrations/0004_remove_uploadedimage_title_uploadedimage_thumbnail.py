# Generated by Django 5.1.7 on 2025-03-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_remove_uploadedimage_thumbnail_uploadedimage_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedimage',
            name='title',
        ),
        migrations.AddField(
            model_name='uploadedimage',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]
