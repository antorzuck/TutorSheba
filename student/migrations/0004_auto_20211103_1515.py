# Generated by Django 3.2.7 on 2021-11-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.FileField(default='static/stud.jpg', null=True, upload_to='media/students'),
        ),
    ]
