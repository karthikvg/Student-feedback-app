from django.urls import path

from form.views.views import *

app_name = 'form'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('student_home/',StudentHome.as_view(),name='student_home'),
    path('write/', ProfessorsList.as_view(), name='write'),
    path('writefeedback/<int:professors_id>/',Feedback.as_view(), name='writefeedback'),
    path('about/',About.as_view(),name='about'),
    path('student_login/',StudentLogin.as_view(),name='student_login'),
    path('student_signup/',SignUp.as_view(),name='signup'),
    path('professor_login/',ProfessorLogin.as_view(),name='professor_login'),
    path('professor_home/',ProfessorHome.as_view(),name='professor_home'),
    path('logout/',LogOut.as_view(), name='logout'),
]
