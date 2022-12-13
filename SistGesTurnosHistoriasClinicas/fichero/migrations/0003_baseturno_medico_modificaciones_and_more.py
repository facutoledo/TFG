# Generated by Django 4.0.6 on 2022-12-13 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fichero', '0002_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTurno',
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
                ('estado', models.CharField(choices=[('AUSENTE', 'Ausente'), ('EN ESPERA', 'En espera'), ('ATENDIENDO', 'Atendiendo'), ('ATENDIDO', 'Atendido')], max_length=50, verbose_name='ESTADO')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='OBSERVACIONES')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='medico',
            name='modificaciones',
            field=models.TextField(default='', verbose_name='MODIFICACIONES'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='modificado_fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='modificado_fecha',
            field=models.DateTimeField(blank=True, null=True),
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
        migrations.CreateModel(
            name='TurnoEstudio',
            fields=[
                ('baseturno_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fichero.baseturno')),
                ('nombre_estudio', models.TextField(blank=True, null=True, verbose_name='NOMBRE_ESTUDIO')),
                ('ubicacion_archivo', models.TextField(blank=True, null=True, verbose_name='UBICACIÓN_ARCHIVO')),
                ('hash_archivo', models.TextField(blank=True, null=True, verbose_name='HASH_ARCHIVO')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudio_medico_related', to='fichero.medico', verbose_name='MEDICO')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudio_paciente_related', to='fichero.paciente', verbose_name='PACIENTE')),
            ],
            options={
                'abstract': False,
            },
            bases=('fichero.baseturno',),
        ),
        migrations.CreateModel(
            name='TurnoConsultorio',
            fields=[
                ('baseturno_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fichero.baseturno')),
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
            bases=('fichero.baseturno',),
        ),
    ]
