# Generated by Django 5.0.6 on 2024-05-26 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_compra_fechacompra_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 20, 17, 40, 618)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 20, 17, 40, 618)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 25, 20, 17, 40, 618)),
        ),
    ]
