# Generated by Django 4.2.4 on 2023-08-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_mainpost_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mainpost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
