from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    return render(request ,"list_task.html")

def create_task(request):
    task = Task(title=request.POST["title"], description=request.POST["description"], time_to_do=request.POST["time_to_do"])
    task.save()
    return redirect("/tasks/")