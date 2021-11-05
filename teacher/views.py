from django.shortcuts import render
from account.models import *
from teacher.models import *
from student.models import *
from account.decorators import *
from django.contrib import messages

@teacher_only
def updateProfile(request):
	loguser = request.user
	teacher = Teacher.objects.get(user=loguser)
	subject = Subject.objects.all()
	if request.method == 'POST':
		teacher.user = request.user
		pro_pic = request.FILES.get('dp')
		if pro_pic:
			teacher.profile_pic = pro_pic
		teacher.city = request.POST.get('c')
		su = request.POST.get('su', None)
		if su:
			teacher.subjects = Subject.objects.get(name=su)
		teacher.bio = request.POST.get('bio')
		teacher.save()
		messages.success(request, 'profile info update successfully!')
		return redirect('/')
	context = {'t':teacher, 's':subject}
	return render(request, 'teacher/update.html', context)
	
	
	
@teacher_only
def hireInfo(request):
	orders = Order.objects.filter(teacher=request.user)
	context = {
			'orders': orders,
	}
	return render(request, 'teacher/hireinfo.html', context)
	
@teacher_only
def acceptOrder(request, id):
	if request.method == 'POST':
		getOrder = Order.objects.get(id=id)
		getOrder.status = True
		getOrder.save()
		messages.success(request, 'you accept the order')
		return redirect(hireInfo)
		
@teacher_only
def showPost(request):
	posts = Post.objects.all().order_by('-id')
	context ={'posts':posts}
	return render(request, 'teacher/posts.html',context)