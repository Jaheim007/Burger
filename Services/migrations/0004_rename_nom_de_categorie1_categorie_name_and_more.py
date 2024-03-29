# Generated by Django 4.2.2 on 2023-06-26 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_alter_plat_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='nom_de_categorie1',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='nom_de_categorie2',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='nom_de_categorie3',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='nom_de_categorie4',
        ),
        migrations.AddField(
            model_name='plat',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Services.categorie'),
        ),
    ]
