# Generated by Django 5.0 on 2023-12-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depenses', '0005_alter_spend_actif_alter_spend_type_depense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spend',
            name='actif',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Citroen Jumper', 'CITROEN JUMPER'), ('Ford', 'FORD'), ('autres', 'autres'), ('usine', 'usine')], max_length=200, null=True),
        ),
    ]
