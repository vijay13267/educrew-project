# Generated by Django 3.1 on 2020-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educrew', '0034_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profilepic.jpg', null=True, upload_to='users/'),
        ),
    ]
