# Generated by Django 5.0.6 on 2024-07-05 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECC', '0004_remove_usuario_id_genero_remove_order_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(db_column='idGenero', primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('activo', models.BooleanField()),
                ('id_genero', models.ForeignKey(db_column='IDGenero', on_delete=django.db.models.deletion.CASCADE, to='ECC.genero')),
            ],
        ),
    ]
