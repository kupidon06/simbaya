# Generated by Django 5.0 on 2024-01-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0033_alter_pers_poste_alter_pers_regime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='poste',
            field=models.CharField(choices=[('Ouvrier', 'Ouvrier'), ('Vendeur', 'vendeur'), ('Chauffeur', 'chauffeur')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pers',
            name='situation',
            field=models.CharField(choices=[('Celibataire', 'celibataire'), ('Marié', 'Marié')], max_length=500, null=True),
        ),
    ]
