# Generated by Django 4.0.4 on 2022-10-25 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_tkycdetalle_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='tkyccabecera',
            name='banco_cuenta',
            field=models.TextField(blank=True, help_text='detalle de informacion bancaria asociada al KYC', max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='tkyccabecera',
            name='fecha_registro',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='fecha de registro'),
        ),
    ]
