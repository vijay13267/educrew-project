# Generated by Django 3.1 on 2020-11-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0012_auto_20201116_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectinfo',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
