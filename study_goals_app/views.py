from django.shortcuts import render
from django.http import HttpResponse
from study_goals_app.models import Study_Goal, Study_Goal_Attachment,Related_Task

# Create your views here.

def Study_goals(request):
    dict = {'inser_here': 'this is views.py', 'vSG':'a', 'VSGD': 'b', 'ESG': 'c', 'NSG': 'd'}
    return HttpResponse("Hello from Study goals")

    return render(request, 'study_goals_app/study_goals.html', context=dict)