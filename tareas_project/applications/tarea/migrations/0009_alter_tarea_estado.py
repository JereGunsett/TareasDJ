# Generated by Django 3.2 on 2024-03-01 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0008_alter_tarea_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completada', 'Completada')], default='Pendiente', max_length=20),
        ),
    ]
