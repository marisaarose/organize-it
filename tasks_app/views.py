from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tasks_app.models import Task, Task_Attachment
from tasks_app.forms import TaskForm

# Create your views here.

def view_tasks(request):
    tasks_list = Task.objects.order_by('due_date')
    task_dict = {'task': tasks_list}
    return render(request, 'tasks_app/view-tasks.html', context = task_dict)

def get_task(request):
    context = {}
 
    # Create a form instance from POST data.
    form = TaskForm(request.POST)
     
    # Check if form data is valid
    if form.is_valid():
        # Save the form data to model
        form.save()
 
    context['form'] = form
    return render(request, "tasks_app/new-task.html", context)