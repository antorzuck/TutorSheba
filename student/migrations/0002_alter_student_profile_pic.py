# Generated by Django 3.2.7 on 2021-11-02 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(default='media/stud.jpg', upload_to='media/students'),
        ),
    ]
