from django.shortcuts import render, redirect
from account.models import *
from teacher.models import *
from student.models import *
from account.decorators import *
from django.contrib import messages
# Create your views here.
@student_only
def hiringInfo(request):
	allOrders = Order.objects.filter(student=request.user).order_by('-id')
	context = { 'allorders': allOrders }
	return render(request, 'student/hireinfo.html', context)
	
@login_user_only
@student_only
def hireTeacher(request, username):
	teacher = User.objects.get(username=username)
	if request.method == 'POST':
		teacher = teacher
		student = request.user
		getCity = request.POST['c']
		getDays = request.POST['d']
		getSellery = request.POST['s']
		
		getOrder = Order(
		teacher=teacher,
		student = student,
		city = getCity,
		days = getDays,
		sellery = getSellery,
		)
		getOrder.save()
		messages.success(request, 'your offer successfully sent to the teacher')
		return redirect('/')
	
	context = {'teacher':teacher}
	return render(request, 'student/hireform.html', context)
	
	
@student_only
def post(request):
	if request.method == 'POST':
		city = request.POST['c']
		sellery = request.POST['s']
		text = request.POST['t']
		
		posted = Post(user=request.user, city=city, sellery=sellery, body=text)
		posted.save()
		messages.success(request, 'your post published successfully, wait for teachers contact you!')
		return redirect('/')
	return render(request, 'student/post.html')
	
	
@student_only
def updateStudent(request):
	loguser = request.user
	student = Student.objects.get(user=loguser)
	if request.method == 'POST':
		student.user = request.user
		pro_pic = request.FILES.get('dp')
		if pro_pic:
			student.profile_pic = pro_pic
		student.city = request.POST.get('c')
		student.bio = request.POST.get('bio')
		student.save()
		messages.success(request, 'profile info update successfully!')
		return redirect('/')
	context = {'student':student}
	return render(request, 'student/update.html', context)
	
		
		
