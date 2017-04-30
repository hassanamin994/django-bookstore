from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms.login_form import LoginForm
from .forms.registeration_form import RegisterationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.
# inserts a user instance into the database
def generate_user(userData):
    user = User.objects.create_user(
        username = userData['username'],
        password = userData['password'],
        first_name = userData['first_name'],
        last_name = userData['last_name'],
        email = userData['email']
        )
    return True

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        return redirect('/app/home/')
    else:
        form = LoginForm()
        # return HttpResponse('hello world')
    return render(request, 'login.html', {'form': form })

def register_view(request):
    errors = []
    if request.method == 'POST':
        userData = request.POST
        errors = []
        form = RegisterationForm(request.POST)
        ###################
        ## form validation
        ###################
        # check for password confirmation
        if userData['password'] != userData['confirm_password']:
            errors.append('Passwords doesnt match ')
        # check for duplicate username
        if User.objects.filter(username=userData['username']).exists():
            errors.append('Username already exists')
        # check for duplicate email
        if User.objects.filter(email=userData['email']).exists():
            errors.append('Email already exists')
        # if no errors are detected, create the user
        if len(errors) == 0 and form.is_valid():
            if generate_user(userData):
                return redirect('/auth/login/')
        # end request.method
    else:
        form = RegisterationForm()

    return render(request, 'registeration.html',{ 'form': form, 'errors': errors })

def logout_view(request):
    logout(request)
    return redirect('/auth/login/')
