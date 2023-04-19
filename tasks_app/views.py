from django.shortcuts import render
from django.http import HttpResponse
from tasks_app.models import Task, Task_Attachment

# Create your views here.

def view_tasks(request):
    tasks_list = Task.objects.order_by('title')
    task_dict = {'task': tasks_list}
    return render(request, 'tasks_app/view-tasks.html', context = task_dict)