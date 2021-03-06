# Generated by Django 3.1 on 2020-11-17 17:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0031_announcements_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='dept_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educrew.dept'),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
