# Generated by Django 4.0.4 on 2022-05-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_merge_20220416_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='es_nuevo',
            field=models.BooleanField(default=False),
        ),
    ]