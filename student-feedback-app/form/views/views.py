from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from form.forms import *


# Home page of the app
from form.models import *


class Home(TemplateView):
    template_name = 'form/home.html'


class ProfessorHome(TemplateView):
    login_url = '/professor_login/'
    template_name = 'form/professor_home.html'
    model = Message

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfessorHome, self).get_context_data(**kwargs)
        temp = Professor.objects.get(roll_no=self.request.user.username)
        context['Messages'] = Message.objects.filter(professor_roll_no=temp).values().order_by('-date')
        return context

class Feedback(TemplateView):
    template_name = "form/writefeedback.html"
    login_url = '/student_login/'
    def get(self,request,**kwargs):
        form = FeedbackForm()
        return render(
            request,
            template_name='form/writefeedback.html',
            context={
                'form': form
            }
        )

    def post(self, request, **kwargs):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            feedback = form.cleaned_data.get('feed_back')
            user=None
            student=Student.objects.get(roll_no=self.request.user.username)
            professor=Professor.objects.get(roll_no=kwargs['professors_id'])
            data = Message.objects.create(title=title,feed_back=feedback,student_roll_no=student,professor_roll_no=professor,date=datetime.now())
            return redirect("form:student_home")


# A temporary pass page
class StudentHome(LoginRequiredMixin, TemplateView):
    login_url = '/student_login/'
    template_name = 'form/student_home.html'
    model = Message

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentHome, self).get_context_data(**kwargs)
        temp=Student.objects.get(roll_no=self.request.user.username)
        context['Messages'] = Message.objects.filter(student_roll_no=temp).values().order_by('-date')
        return context


# After student login to his account he can view the home page here
class ProfessorsList(ListView):
    login_url = '/student_login/'
    template_name = 'form/Professors.html'
    model = Professor

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfessorsList, self).get_context_data(**kwargs)
        context['Professors'] = Professor.objects.values()
        return context


# Description about the app
class About(TemplateView):
    template_name = 'form/about.html'


class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('form:student_login')


# Student login page
class ProfessorLogin(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(
            request,
            template_name='form/professor_login.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):

        form = LogInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            professor=Professor.objects.filter(roll_no=username)
            if user is not None and professor:
                login(request, user)
                return redirect('form:professor_home')
            else:
                return redirect('form:professor_login')


class StudentLogin(View):
    def get(self, request, *args, **kwargs):
        form = LogInForm()
        return render(
            request,
            template_name='form/student_login.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = LogInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and len(Student.objects.filter(roll_no=username)) !=0:
                login(request, user)
                return redirect('form:student_home')
            else:
                return redirect('form:student_login')


# Student signup page
class SignUp(View):
    def get(self, request):
        form = SignUpForm(None)
        return render(request, template_name='form/student_registration.html', context={'form': form})

    def post(self, request, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['roll_no'],
                                            password=form.cleaned_data['password'])
            Student.objects.create(roll_no=form.cleaned_data['roll_no'],first_name=form.cleaned_data['first_name'],
                                   middle_name=form.cleaned_data['middle_name'],last_name=form.cleaned_data['last_name'],
                                   password=form.cleaned_data['password'],email_id=form.cleaned_data['email_id'],
                                   picture=form.cleaned_data['picture'])
            user.set_password(form.cleaned_data['password'])
            user = authenticate(
                request,
                username=form.cleaned_data['roll_no'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('form:student_home')
