from django.db import models
from account.models import *

# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.FileField(upload_to='media/students', default='static/stud.jpg', null=True)
	city = models.CharField(max_length=30, null=True)
	bio = models.TextField(null=True)
	

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	sellery = models.CharField(max_length=5)
	city = models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.user)
	
	
class Order(models.Model):
	teacher = models.ForeignKey(User, on_delete= models.CASCADE, related_name='teacherorder')
	student = models.ForeignKey(User, on_delete= models.CASCADE, related_name='studentorder')
	city = models.CharField(max_length=30)
	sellery = models.CharField(max_length=5)
	days = models.CharField(max_length=50)
	status = models.BooleanField(default=False)
	
	def __str__(self):
		return str(self.teacher)