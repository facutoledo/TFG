# Generated by Django 3.2.5 on 2021-07-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autenticacion', '0002_auto_20210719_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.CharField(max_length=255, unique=True, verbose_name='DNI'),
        ),
    ]
