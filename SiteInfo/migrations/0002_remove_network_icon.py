# Generated by Django 4.0.4 on 2022-05-17 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SiteInfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='network',
            name='Icon',
        ),
    ]
