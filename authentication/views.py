from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        fisrtname = request.POST['fisrtname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fisrtname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request,'Your Account has been successfully created')

        return redirect('signin')
    return render(request, 'authentication/index.html')


def signup(request):
    return render(request, 'authentication/signup.html')


def signin(request):
    return render(request, 'authentication/signin.html')


def logout(request):
    return render(request, 'authentication/logout.html')
