# Generated by Django 3.2 on 2024-02-20 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0007_alter_proyecto_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(default=datetime.date(2024, 2, 20)),
        ),
    ]
