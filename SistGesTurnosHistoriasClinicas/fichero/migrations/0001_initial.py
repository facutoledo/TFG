# Generated by Django 4.0.6 on 2022-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(auto_now=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('dni', models.CharField(max_length=50, unique=True, verbose_name='DNI')),
                ('apellido', models.CharField(max_length=150, verbose_name='APELLIDO')),
                ('nombre', models.CharField(max_length=150, verbose_name='NOMBRE')),
                ('fecha_de_nacimiento', models.DateField(verbose_name='NACIMIENTO')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='CORREO_ELECTRONICO')),
                ('pais', models.CharField(max_length=50, verbose_name='PAIS')),
                ('provincia', models.CharField(max_length=50, verbose_name='PROVINCIA')),
                ('localidad', models.CharField(max_length=50, verbose_name='LOCALIDAD')),
                ('direccion', models.CharField(max_length=50, verbose_name='DIRECCION')),
                ('telefono', models.CharField(max_length=50, verbose_name='TELEFONO')),
                ('contacto', models.CharField(max_length=150, verbose_name='CONTACTO')),
                ('antecedentes', models.TextField(default='', null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]