# Generated by Django 5.0 on 2024-01-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0034_alter_pers_poste_alter_pers_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='poste',
            field=models.CharField(choices=[('Chauffeur', 'chauffeur'), ('Vendeur', 'vendeur'), ('Ouvrier', 'Ouvrier')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pers',
            name='regime',
            field=models.CharField(choices=[('Pourcentage', 'Pourcentage'), ('Salarié', 'salarié')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pers',
            name='situation',
            field=models.CharField(choices=[('Marié', 'Marié'), ('Celibataire', 'celibataire')], max_length=500, null=True),
        ),
    ]
