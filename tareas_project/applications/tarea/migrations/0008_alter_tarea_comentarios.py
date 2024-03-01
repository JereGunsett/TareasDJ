# Generated by Django 3.2 on 2024-02-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0003_alter_comentario_autor'),
        ('tarea', '0007_alter_tarea_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='comentarios',
            field=models.ManyToManyField(blank=True, related_name='comentarios', to='comentario.Comentario'),
        ),
    ]