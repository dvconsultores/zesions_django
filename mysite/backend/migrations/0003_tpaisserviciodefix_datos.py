# Generated by Django 4.0.4 on 2022-10-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_tpaisserviciodefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='tpaisserviciodefix',
            name='datos',
            field=models.TextField(blank=True, help_text='Detalle de infirmacion de FIAT x Pais', max_length=200, null=True),
        ),
    ]
