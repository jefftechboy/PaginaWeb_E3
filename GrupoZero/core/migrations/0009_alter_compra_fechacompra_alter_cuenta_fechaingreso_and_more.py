# Generated by Django 5.0.1 on 2024-05-22 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_compra_fechacompra_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 11, 26, 16, 514331)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 11, 26, 16, 512330)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 11, 26, 16, 513331)),
        ),
    ]