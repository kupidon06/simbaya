# Generated by Django 5.0 on 2024-01-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0024_alter_pers_poste_alter_pers_situation'),
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
            field=models.CharField(choices=[('Celibataire', 'celibataire'), ('Marié', 'Marié')], max_length=500, null=True),
        ),
    ]