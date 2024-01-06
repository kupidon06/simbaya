# Generated by Django 5.0 on 2023-12-31 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0008_alter_spend_actif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='actif',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('usine', 'usine'), ('Citroen Jumper', 'CITROEN JUMPER'), ('Ford', 'FORD'), ('autres', 'autres')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='spend',
            name='type_depense',
            field=models.CharField(blank=True, choices=[('charge ordinaire', 'charge ordinaire'), ('charge familliale', 'charge familliale')], max_length=200, null=True),
        ),
    ]
