# Generated by Django 4.0.4 on 2022-11-10 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0047_fiattransaccion_adjuntofiat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiattransaccion',
            name='adjuntofiat',
        ),
    ]
