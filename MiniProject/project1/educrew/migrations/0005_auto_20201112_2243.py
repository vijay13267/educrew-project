# Generated by Django 3.1.3 on 2020-11-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0004_auto_20201112_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_name',
            field=models.CharField(max_length=50),
        ),
    ]