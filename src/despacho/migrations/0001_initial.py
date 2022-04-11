# Generated by Django 4.0.3 on 2022-04-11 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=200, verbose_name='calle')),
                ('numero', models.CharField(max_length=200, verbose_name='numero')),
                ('departamento', models.CharField(blank=True, max_length=200, verbose_name='departamento')),
                ('piso', models.CharField(blank=True, max_length=200, null=True, verbose_name='piso')),
                ('region', models.CharField(max_length=200, verbose_name='region')),
                ('ciudad', models.CharField(max_length=200, verbose_name='cuidad')),
                ('codigo_postal', models.CharField(max_length=200, verbose_name='codigo postal')),
                ('telefono', models.IntegerField(verbose_name='telefono')),
                ('estado', models.PositiveSmallIntegerField(choices=[[1, 'Pendiente'], [2, 'En_proceso'], [3, 'Finalizado'], [4, 'Fallido']], default=1)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]