# Generated by Django 5.0 on 2024-01-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0029_alter_pers_poste_alter_pers_situation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pers',
            name='poste',
            field=models.CharField(choices=[('Vendeur', 'vendeur'), ('Chauffeur', 'chauffeur'), ('Ouvrier', 'Ouvrier')], max_length=200, null=True),
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
