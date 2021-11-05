from django.db import models
from account.models import *

# Create your models here.
class Subject(models.Model):
	name = models.CharField(max_length=20)
	thumbnail = models.FileField(upload_to='media/category')
	
	def __str__(self):
		return self.name

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.FileField(upload_to='media/teacher', default='static/stud.jpg', null=True)
	is_verified= models.BooleanField(default=False)
	city = models.CharField(max_length=50, null=True)
	bio= models.TextField(null=True)
	subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.user)
	
