from django.shortcuts import render
from teacher.models import *
from account.decorators import *
from django.contrib import messages
from django.contrib import auth
from account.models import *
from student.models import *
# Create your views here.

def home(request):
	allCategory = Subject.objects.all()
	verifiedTeacher = Teacher.objects.filter(is_verified=True)
	context={
			'allcats':allCategory,
			'verified': verifiedTeacher
	}
	return render(request, 'home.html', context)



@if_not_login
def handleLogin(request):
	if request.method == 'POST':
		username = request.POST['un']
		password = request.POST['p']
		
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.success(request, 'Successfully Login!')
			return redirect('/')
	return render(request, 'login.html')
	
	
@if_not_login
def handleSignUp(request):
	if request.method == 'POST':
		username = request.POST['un']
		password1 = request.POST['up']
		password2 = request.POST['upc']
		select = request.POST['sl']
		
		if password1 != password2:
			messages.error(request, 'Password not matched!')
			return render(request, 'join.html')
		if len(username) < 5:
			messages.error(request, 'Username must be 5 character long!')
			return render(request, 'join.html')
		try:
			user = User.objects.get(username=username)
			messages.error(request, 'Username already taken!')
			return render(request, 'join.html')
		except User.DoesNotExist:
			if select == 'Teacher':
				user = User.objects.create_user(username=username, password=password1)
				user.is_teacher = True
				user.save()
				teacher = Teacher.objects.create(user= user)
				teacher.save()
				auth.login(request, user)
				messages.success(request, 'your teacher accounr created successfully!')
				return redirect('/')
			else:
				user = User.objects.create_user(username=username, password=password1)
				user.is_student = True
				user.save()
				student = Student.objects.create(user=user)
				student.save()
				auth.login(request, user)
				messages.success(request, 'your student account created successfully')
				return redirect('/')
			
	return render(request, 'join.html')



def handleLogOut(request):
	auth.logout(request)
	messages.success(request, 'you logged out!')
	return redirect('/')


def handleSearch(request):
	if request.method == 'POST':
		query = request.POST['q']
		teachers = Teacher.objects.filter(city__icontains=query)
		
		count = teachers.count()
		context={
				'count': count,
				'query': query,
				'teachers': teachers
		}
		return render(request, 'search.html', context)
		
		
		
def subjects(request, id):
	subject = Subject.objects.get(id=id)
	teachers = Teacher.objects.filter(subjects=subject)
	count = teachers.count()
	context={
		'count': count,
		'subject': subject,
		'teachers': teachers
	}
	return render(request, 'subject.html', context)
	