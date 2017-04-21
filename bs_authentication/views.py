from django.shortcuts import render
from django.http import HttpResponse
from .forms.login_form import LoginForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
        # return HttpResponse('hello world')
    return render(request, 'login.html', {'form': form })
