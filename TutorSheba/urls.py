from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from account.views import *
from teacher.views import *
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('login', handleLogin, name='login'),
    path('join', handleSignUp, name='join'),
    path('logout', handleLogOut, name='logout'),
    
    path('search', handleSearch, name='search'),
    path('subjects/<id>', subjects, name='subjects'),
    
    path('teacher-update', updateProfile, name='tupdate'),
    path('student-update', updateStudent, name='supdate'),
    
    path('student-hire', hiringInfo, name='hsInfo'),
    path('teacher-hire', hireInfo, name='htInfo'),
    path('accept-order/<id>', acceptOrder, name='acceptorder'),
    path('hire/<username>', hireTeacher, name='hire'),
    
    path('post', post, name='post'),
    path('students-post', showPost, name='spost')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
