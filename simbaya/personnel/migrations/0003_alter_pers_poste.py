# Generated by Django 5.0 on 2023-12-25 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0002_alter_pers_poste_alter_pers_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='poste',
            field=models.CharField(choices=[('Ouvrier', 'Ouvrier'), ('Chauffeur', 'chauffeur'), ('Vendeur', 'vendeur')], max_length=200, null=True),
        ),
    ]