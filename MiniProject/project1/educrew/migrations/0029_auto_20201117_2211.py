# Generated by Django 3.1 on 2020-11-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0028_auto_20201117_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='date',
            field=models.DateField(null=True),
        ),
    ]