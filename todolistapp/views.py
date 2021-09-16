from django.shortcuts import render, HttpResponse, redirect
from todolistapp.models import Task
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login



# Create your views here.

def home(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        desc = request.POST.get('dis')
        ins = Task(taskTitle=title, taskDis=desc)
        ins.save()
        messages.success(request,'Task has been added :)')


    return render(request, 'index.html')

def task(request):
    allTask = Task.objects.all()
    context = {'tasks':allTask}

    return render(request, 'task.html',context)


def deletet(request,id):
    Task.objects.filter(id=id).delete()
    messages.success(request,"Task Deleted success !")

    return redirect('task')


