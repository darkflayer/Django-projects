from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
def home(reqest):
    return HttpResponse("Hello, World!")

def welcome(request):
    return HttpResponse("Welcome to my Django App bro!")

def task_list(request):
    '''
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        if title:
            Task.objects.create(title=title,description=description)
            return redirect('task_list')
    tasks=Task.objects.all() #Get all tasks from the database
    return render(request,'todo/task_list.html',{'tasks':tasks})'''
    
    tasks=Task.objects.all()
    form=TaskForm()
    
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request,'todo/task_list.html',{'tasks':tasks,'form':form})
    
def toggle_completion(request,task_id):
    task=Task.objects.get(id=task_id)
    task.completed=not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Find the task
    task.delete()  # Delete it from the database
    return redirect("task_list")  # Refresh the page

