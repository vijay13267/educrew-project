# Generated by Django 3.1 on 2020-11-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0014_studentschedule_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentschedule',
            name='p1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentschedule',
            name='p4',
            field=models.IntegerField(null=True),
        ),
    ]