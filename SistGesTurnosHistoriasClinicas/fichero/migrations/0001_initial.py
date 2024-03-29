# Generated by Django 4.0.6 on 2022-12-14 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(blank=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
                ('dni', models.CharField(max_length=50, unique=True, verbose_name='DNI')),
                ('apellido', models.CharField(max_length=150, verbose_name='APELLIDO')),
                ('nombre', models.CharField(max_length=150, verbose_name='NOMBRE')),
                ('correo_electronico', models.EmailField(max_length=254, verbose_name='CORREO_ELECTRONICO')),
                ('telefono', models.CharField(max_length=50, verbose_name='TELEFONO')),
                ('matricula', models.CharField(max_length=50, verbose_name='MATRICULA_PROFESIONAL')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(blank=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
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
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TurnoEstudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(blank=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
                ('fecha', models.DateField(verbose_name='FECHA')),
                ('hora', models.TimeField(verbose_name='HORA')),
                ('estado', models.CharField(choices=[('AUSENTE', 'Ausente'), ('EN ESPERA', 'En espera'), ('ATENDIENDO', 'Atendiendo'), ('ATENDIDO', 'Atendido')], default='AUSENTE', max_length=50, verbose_name='ESTADO')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='OBSERVACIONES')),
                ('nombre_estudio', models.TextField(blank=True, null=True, verbose_name='NOMBRE_ESTUDIO')),
                ('ubicacion_archivo', models.TextField(blank=True, null=True, verbose_name='UBICACIÓN_ARCHIVO')),
                ('hash_archivo', models.TextField(blank=True, null=True, verbose_name='HASH_ARCHIVO')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudio_medico_related', to='fichero.medico', verbose_name='MEDICO')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudio_paciente_related', to='fichero.paciente', verbose_name='PACIENTE')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TurnoConsultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(blank=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
                ('fecha', models.DateField(verbose_name='FECHA')),
                ('hora', models.TimeField(verbose_name='HORA')),
                ('estado', models.CharField(choices=[('AUSENTE', 'Ausente'), ('EN ESPERA', 'En espera'), ('ATENDIENDO', 'Atendiendo'), ('ATENDIDO', 'Atendido')], default='AUSENTE', max_length=50, verbose_name='ESTADO')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='OBSERVACIONES')),
                ('mediciones_realizadas', models.TextField(blank=True, null=True, verbose_name='MEDICIONES_REALIZADAS')),
                ('motivo_consulta', models.TextField(blank=True, null=True, verbose_name='MOTIVO_CONSULTA')),
                ('diagnostico', models.TextField(blank=True, null=True, verbose_name='DIAGNOSTICO')),
                ('tratamiento', models.TextField(blank=True, null=True, verbose_name='TRATAMIENTO')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultorio_medico_related', to='fichero.medico', verbose_name='MEDICO')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultorio_paciente_related', to='fichero.paciente', verbose_name='PACIENTE')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrado', models.BooleanField(default=False)),
                ('creado_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('creado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificado_fecha', models.DateTimeField(blank=True, null=True)),
                ('modificado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('borrado_fecha', models.DateTimeField(blank=True, null=True)),
                ('borrado_usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('modificaciones', models.TextField(default='', verbose_name='MODIFICACIONES')),
                ('ubicacion_archivo', models.TextField(verbose_name='UBICACIÓN_ARCHIVO')),
                ('hash_archivo', models.TextField(verbose_name='HASH_ARCHIVO')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='OBSERVACIONES')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HisClin_paciente_related', to='fichero.paciente', verbose_name='PACIENTE')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
