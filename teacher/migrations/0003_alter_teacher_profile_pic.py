# Generated by Django 3.2.7 on 2021-11-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20211102_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='profile_pic',
            field=models.FileField(default='static/stud.jpg', upload_to='media/teacher'),
        ),
    ]
