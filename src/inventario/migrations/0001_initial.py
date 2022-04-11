# Generated by Django 4.0.3 on 2022-04-10 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=200, verbose_name='apellido')),
                ('es_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('editorial', models.CharField(max_length=200, verbose_name='editorial')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='genero')),
            ],
        ),
        migrations.CreateModel(
            name='IVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iva', models.IntegerField(verbose_name='iva')),
            ],
        ),
        migrations.CreateModel(
            name='OtrosAutores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='nombre')),
                ('cargo', models.CharField(max_length=200, verbose_name='cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=200, verbose_name='pais')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=200, unique=True, verbose_name='isbn')),
                ('titulo_es', models.CharField(max_length=200, verbose_name='titulo')),
                ('titulo_jp', models.CharField(blank=True, max_length=200, verbose_name='titulo jp')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('portada', models.CharField(max_length=200, verbose_name='ruta de portada portada')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='precio')),
                ('descripcion', models.CharField(blank=True, max_length=200, verbose_name='descripcion')),
                ('numero_paginas', models.IntegerField(verbose_name='numero de paginas')),
                ('es_color', models.BooleanField(default=False)),
                ('fecha_publicacion', models.DateField(verbose_name='fecha de publicacion')),
                ('esta_publicado', models.BooleanField(default=False)),
                ('es_destacado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.editorial')),
                ('genero', models.ManyToManyField(to='inventario.genero', verbose_name='genero')),
                ('iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.iva')),
                ('oferta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.oferta')),
                ('otros_autores', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.otrosautores')),
            ],
        ),
        migrations.AddField(
            model_name='editorial',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.pais'),
        ),
    ]
