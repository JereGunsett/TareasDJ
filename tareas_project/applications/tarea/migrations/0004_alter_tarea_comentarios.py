# Generated by Django 3.2 on 2024-02-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0002_alter_comentario_tarea'),
        ('tarea', '0003_tarea_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='comentarios',
            field=models.ManyToManyField(related_name='comentarios', to='comentario.Comentario'),
        ),
    ]
