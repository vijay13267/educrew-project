# Generated by Django 3.1.3 on 2020-11-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0008_auto_20201112_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturerschedule',
            name='lect_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='educrew.lecturer'),
        ),
    ]
