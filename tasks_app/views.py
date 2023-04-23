from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from tasks_app.models import Task, Task_Attachment
from tasks_app.forms import TaskForm, Task_AttachmentForm

# Create your views here.

def view_tasks(request):
    tasks_list = Task.objects.order_by('due_date').filter(is_pinned=False, is_complete=False)
    pinned_list = Task.objects.filter(is_pinned=True)
    compltasks_list = Task.objects.filter(is_complete=True)
    return render(request, 'tasks_app/view-tasks.html', context = {'task':tasks_list,'pinned':pinned_list,'complete':compltasks_list})

def new_task(request):
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            task = Task.objects.latest('task_id')
            return redirect('task details', task.task_id)
    else:
        form = TaskForm()
    context['form'] = form
    return render(request, "tasks_app/new-task.html", context)

def get_task(request, id):
    task = Task.objects.get(task_id = id)
    attachments_list = {}
    
    if Task_Attachment.objects.all():
        attachments_list = Task_Attachment.objects.filter(task_id = id)
        
    return render(request, 'tasks_app/task-details.html', context = {'task': task, 'attachments': attachments_list})

def edit_task(request, id):
    task = Task.objects.get(task_id = id)
    attachments_list = {}
    if Task_Attachment.objects.all():
            attachments_list = Task_Attachment.objects.filter(task_id = id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if form.instance.is_complete == True:
                form.instance.is_pinned = False
            form.save()
            return redirect('task details', task.task_id)
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'tasks_app/edit-task.html', context = {'form': form, 'attachments': attachments_list})

def new_attachment(request, id):
    task = Task.objects.get(task_id = id)
    context = {}
    if request.method == 'POST':
        form = Task_AttachmentForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task details', task.task_id)
    else:
        form = Task_AttachmentForm(initial={'task_id': id})
    context['form'] = form
    return render(request, "tasks_app/new-attachment.html", context)

def delete_attachment(request, id):
    attachment = Task_Attachment.objects.get(attachments_id = id)
    attachment.file.delete()
    attachment.delete()
    return redirect('task details', attachment.task_id.task_id)

def delete_task(request, id):
    task = Task.objects.get(task_id = id)
    task.delete()
    return redirect('view tasks')
    