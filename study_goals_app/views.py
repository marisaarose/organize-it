from django.shortcuts import render
from django.http import HttpResponse
from study_goals_app.models import Study_Goal, Study_Goal_Attachment,Related_Task

# Create your views here.

def Study_goals(request):
    goal_list = Study_Goal.objects.order_by('due_date')
    goal_dict = {'goal': goal_list}

    return render(request, 'study_goals_app/study_goals.html', context=goal_dict)