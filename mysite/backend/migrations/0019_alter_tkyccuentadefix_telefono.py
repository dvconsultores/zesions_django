# Generated by Django 4.0.4 on 2022-11-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_tkyccuentadefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tkyccuentadefix',
            name='telefono',
            field=models.TextField(blank=True, help_text='Numero de telefono del titular', max_length=50, null=True),
        ),
    ]