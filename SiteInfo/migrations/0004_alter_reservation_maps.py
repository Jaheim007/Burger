# Generated by Django 4.0.4 on 2022-05-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteInfo', '0003_reservation_dial_code_alter_reservation_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='Maps',
            field=models.URLField(max_length=255),
        ),
    ]
