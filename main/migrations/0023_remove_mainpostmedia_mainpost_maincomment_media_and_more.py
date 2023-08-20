# Generated by Django 4.2.4 on 2023-08-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_maincomment_media_remove_mainpost_media_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainpostmedia',
            name='mainpost',
        ),
        migrations.AddField(
            model_name='maincomment',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='maincomment_media/'),
        ),
        migrations.AddField(
            model_name='mainpost',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='mainpost_media/'),
        ),
        migrations.DeleteModel(
            name='MainCommentMedia',
        ),
        migrations.DeleteModel(
            name='MainPostMedia',
        ),
    ]
