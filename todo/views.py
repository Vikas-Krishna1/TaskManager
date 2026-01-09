from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.
def signupUser(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request,'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Username already exists Pleasen choose another one'})
        else:
            return render(request,'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords do not match'})
    elif request.method == "GET":
       return render(request,'todo/signupuser.html', {'form':UserCreationForm()})         
def currenttodos(request):
    return render(request,'todo/currenttodos.html')