# Generated by Django 3.2 on 2024-02-09 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0002_rename_asignado_a_tarea_usuario_asignado'),
        ('comentario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_comentarios', to='tarea.tarea'),
        ),
    ]
