# Generated by Django 4.2.4 on 2023-08-18 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_remove_mainpostmedia_mainpost_maincomment_media_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincomment',
            name='media',
        ),
        migrations.RemoveField(
            model_name='mainpost',
            name='media',
        ),
        migrations.CreateModel(
            name='MainPostMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='mainpost_media/')),
                ('mainpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='main.mainpost')),
            ],
        ),
        migrations.CreateModel(
            name='MainCommentMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(blank=True, null=True, upload_to='maincomment_media/')),
                ('MainComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='main.maincomment')),
            ],
        ),
    ]
