# Generated by Django 5.0 on 2024-01-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0017_alter_spend_actif_alter_spend_type_depense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='actif',
            field=models.CharField(choices=[('Ford', 'FORD'), ('Citroen Jumper', 'CITROEN JUMPER'), ('Toyota', 'Toyota'), ('autres', 'autres'), ('usine', 'usine')], max_length=200, null=True),
        ),
    ]
