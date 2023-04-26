from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Study_Goal, Study_Goal_Attachment,Related_Task
from .forms import Study_GoalsForm, Study_Goal_AttachmentForm, Related_TaskForm
# Create your views here.

def Study_goals(request):
    goal_list = Study_Goal.objects.order_by('due_date')
    goal_dict = {'goal': goal_list}

    return render(request, 'study_goals/study_goals.html', context=goal_dict)

def get_goal(request, id):
    goal = Study_Goal.objects.get(Study_Goal_id = id)
    goal_attachment_list = {}
    
    if Study_Goal_Attachment.objects.all():
        goal_attachment_list = Study_Goal_Attachment.objects.filter(Study_Goal_id = id)
        
        return render(request, 'study_goals/study_goals.html', context={'goal': goal, 'attachment': goal_attachment_list})

def edit_study_goals(request, id):
    goal = Study_Goal.objects.get(Study_Goal_id = id)
    
    if request.method == 'POST':
          form = Study_GoalsForm(request.POST, isinstance=goal)
        if form.is_valid():
            if form.instance.is_complete == True:
                form.instance.is_pinned = False
            form.save()
            return redirect('goal details', goal.study_goal_id)
    else:
        form = Study_GoalsForm(instance=goal)
        
    return render(request, 'study_goals_app/edit-goals.html', context = {'form': form,})

def new_study_goals(request):
      context = {}
    if request.method == 'POST':
        form = Study_GoalsForm(request.POST)
        if form.is_valid():
            form.save()
            task = Study_Goal.objects.latest('study_goal_id')
            return redirect('goal details', goal.study_goal_id)
    else:
        form = Study_GoalsForm()
    context['form'] = form
    return render(request, 'study_goals_app/edit-goals.html', context = {'form': form,})


def delete_study_goal(request, id):
    goal = Study_Goal.objects.get(Study_Goal_id = id)
    goal.delete()
    return redirect('view goal')

def get_goal(request, id):
    goal = Study_Goal.objects.get(Study_Goal_id = id)
    
    if Study_Goal_Attachment.object.all():
              attachments_list = Study_Goal_Attachment.objects.filter(Study_Goal_id = id)
    if request.method == 'POST':
        form = Study_GoalsForm(request.POST, instance=goal)
        if form.is_valid():
            if form.instance.is_complete == True:
                form.instance.is_pinned = False
            form.save()
            return redirect('goal details', goal.study_goal_id)
    else:
        form = Study_GoalsForm(instance=goal)
        
    return render(request, 'study_goals_app/edit-goals.html', context = {'form': form, 'attachments': attachments_list})
