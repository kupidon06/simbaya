# Generated by Django 5.0 on 2023-12-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0018_alter_pers_poste_alter_pers_regime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='poste',
            field=models.CharField(choices=[('Chauffeur', 'chauffeur'), ('Ouvrier', 'Ouvrier'), ('Vendeur', 'vendeur')], max_length=200, null=True),
        ),
    ]
