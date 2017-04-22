from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms.login_form import LoginForm
from .forms.registeration_form import RegisterationForm
from django.contrib.auth.models import User
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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
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
            generate_user(userData)
        # end request.method
    else:
        form = RegisterationForm()

    return render(request, 'registeration.html',{ 'form': form, 'errors': errors })
