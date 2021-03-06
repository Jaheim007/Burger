# Generated by Django 4.0.4 on 2022-05-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_de_categorie', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OpenDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jours', models.CharField(max_length=255)),
                ('Dheure', models.TimeField()),
                ('Fheure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=255)),
                ('Description', models.TextField(max_length=500)),
                ('Image', models.ImageField(upload_to='')),
                ('Prix', models.CharField(max_length=255)),
                ('Rprix', models.CharField(max_length=255)),
                ('Boolean', models.BooleanField()),
            ],
        ),
    ]
