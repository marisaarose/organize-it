from django.shortcuts import render
from django.http import HttpResponse
from study_goals_app.models import Study_Goal, Study_Goal_Attachment,Related_Task
from .forms import Study_GoalsForm, Study_Goal_AttachmentForm, Related_TaskForm
# Create your views here.

def Study_goals(request):
    goal_list = Study_Goal.objects.order_by('due_date')
    goal_dict = {'goal': goal_list}

    return render(request, 'study_goals/study_goals.html', context=goal_dict)

def edit_study_goals(request, id):
    goal = Study_Goal.objects.get(Study_Goal_id = id)
    
    if request.method == 'POST':
          form = Study_GoalSForm(request.POST, isinstance=goal)
        if form.is_valid():
            if form.instance.is_complete == True:
                form.instance.is_pinned = False
            form.save()
            return redirect('goal details', goal.study_goal_id)
    else:
        form = Study_GoalsForm(instance=goal)
        
    return render(request, 'study_goals_app/edit-goals.html', context = {'form': form,})