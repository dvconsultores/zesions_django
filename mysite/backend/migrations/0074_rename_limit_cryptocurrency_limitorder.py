# Generated by Django 4.0.4 on 2023-05-03 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0073_cryptocurrency_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptocurrency',
            old_name='limit',
            new_name='limitOrder',
        ),
    ]