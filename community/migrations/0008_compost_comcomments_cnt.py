# Generated by Django 4.2.4 on 2023-08-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_comcomment_compost'),
    ]

    operations = [
        migrations.AddField(
            model_name='compost',
            name='comcomments_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
