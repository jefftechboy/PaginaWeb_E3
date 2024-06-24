# Generated by Django 5.0.6 on 2024-05-24 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_compra_fechacompra_alter_cuenta_fechaingreso_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autentificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCliente', models.CharField(max_length=60)),
                ('Correo', models.CharField(max_length=60)),
                ('Direccion', models.CharField(max_length=60)),
                ('Telefono', models.CharField(max_length=60)),
                ('imagen', models.ImageField(upload_to='obra')),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='fechaCompra',
            field=models.DateField(default=datetime.datetime(2024, 5, 24, 18, 31, 36, 532201)),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 24, 18, 31, 36, 530202)),
        ),
        migrations.AlterField(
            model_name='obra',
            name='fechaIngreso',
            field=models.DateField(default=datetime.datetime(2024, 5, 24, 18, 31, 36, 531201)),
        ),
    ]
