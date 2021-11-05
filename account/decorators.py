from django.shortcuts import render, redirect
from account.views import *


def if_not_login(func):
	def wrap(request, *args, **kwargs):
		if not request.user.is_authenticated:
			return func(request, *args, **kwargs)
		else:
			return redirect('/')
	return wrap
	
def student_only(func):
	def wrap(request, *args, **kwargs):
		if request.user.is_student:
			return func(request, *args, **kwargs)
		else:
			return redirect('/')
	return wrap
	
	
def teacher_only(func):
	def wrap(request, *args, **kwargs):
		if request.user.is_teacher:
			return func(request, *args, **kwargs)
		else:
			return redirect('/')
	return wrap
	
def login_user_only(func):
	def wrap(request, *args, **kwargs):
		if request.user.is_authenticated:
			return func(request, *args, **kwargs)
		else:
			return render(request, 'join.html')
	return wrap