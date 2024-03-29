# Generated by Django 4.0.6 on 2022-12-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=255, unique=True, verbose_name='DNI')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('intentos_fallidos_de_ingreso', models.IntegerField(default=7)),
                ('is_active', models.BooleanField(default=False, verbose_name='Usuario activo')),
                ('fecha_ultimo_cambio_de_contrasena', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuario personal')),
                ('es_paciente', models.BooleanField(default=False, verbose_name='Usuario paciente')),
                ('es_medico', models.BooleanField(default=False, verbose_name='Usuario médico')),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
