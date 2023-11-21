# Generated by Django 4.0.4 on 2023-03-30 15:47

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0070_alter_cryptocurrency_time_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='tdataCrypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, help_text='Nombre del token', max_length=150, null=True)),
                ('token', models.TextField(blank=True, help_text='ruta del token', max_length=150, null=True)),
                ('title', models.TextField(blank=True, help_text='titulo del token', max_length=150, null=True)),
                ('desc', models.TextField(blank=True, help_text='descripcion del token', max_length=150, null=True)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), help_text='monto', max_digits=14)),
                ('state', models.TextField(blank=True, help_text='descripcion del token', max_length=150, null=True)),
                ('colorG', models.BooleanField(default=True, help_text='Esta activo colorG')),
                ('colorR', models.BooleanField(default=True, help_text='Esta activo colorR')),
                ('habilitado', models.BooleanField(default=True, help_text='Esta activo?')),
            ],
        ),
    ]