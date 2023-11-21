# Generated by Django 4.0.4 on 2023-04-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0071_tdatacrypto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdatacrypto',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='tdatacrypto',
            name='colorG',
        ),
        migrations.RemoveField(
            model_name='tdatacrypto',
            name='colorR',
        ),
        migrations.RemoveField(
            model_name='tdatacrypto',
            name='state',
        ),
        migrations.AddField(
            model_name='tdatacrypto',
            name='network',
            field=models.TextField(blank=True, help_text='descripcion de la red', max_length=150, null=True),
        ),
    ]
