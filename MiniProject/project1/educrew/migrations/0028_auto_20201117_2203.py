# Generated by Django 3.1 on 2020-11-17 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0027_auto_20201117_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 17, 22, 3, 19, 719072), null=True),
        ),
    ]
