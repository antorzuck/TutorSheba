# Generated by Django 3.2.7 on 2021-11-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(default='static/stud.jpg', upload_to='media/students'),
        ),
    ]
