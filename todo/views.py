from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request):
    return render(request,'todo/home.html')

##Aunth Views
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

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
def loginuser(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            return render(
                request,
                'todo/loginuser.html',
                {
                    'form': AuthenticationForm(),
                    'error': 'Username or Password is incorrect. Please try again!'
                }
            )
        else:
            login(request, user)
            return redirect('currenttodos')

    else:
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})

    

#_______________________________________________________________________    


    
##Todo Views
@login_required
def createtodo(request):
    if request.method == "GET":
        return render(request,'todo/createtodo.html', {'form':TodoForm()})
    elif request.method == "POST":
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
             return render(request,'todo/createtodo.html', {'form':TodoForm(),'error':'Bad data passed in. Try Again'})
@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user = request.user, dateTimeCompleted__isnull=True)
    return render(request,'todo/currenttodos.html', {'todos':todos})
@login_required
def viewtodo(request,todo_pk):   
    todo = get_object_or_404(Todo,pk=todo_pk ,user=request.user)
    if request.method=="GET":
        form = TodoForm(instance=todo)
        return render(request,'todo/viewtodo.html',{'todo':todo,'form':form})
    elif request.method=="POST":
        try:
            form = TodoForm(request.POST,instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
             return render(request,'todo/viewtodo.html',{'todo':todo,'form':form,'error':'Bad data passed in. Try Again'})
@login_required
def completetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk ,user=request.user)
    if request.method=="POST":
        todo.dateTimeCompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')
@login_required
def deletetodo(request,todo_pk):
    todo = get_object_or_404(Todo,pk=todo_pk ,user=request.user)
    if request.method=="POST":
        todo.delete()
        return redirect('currenttodos')
@login_required

def completedtodos(request):
    todos = Todo.objects.filter(user = request.user, dateTimeCompleted__isnull=False).order_by('-dateTimeCompleted')
    return render(request,'todo/completedtodos.html', {'todos':todos})
   

        
       