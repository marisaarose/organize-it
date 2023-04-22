from django.urls import path
from study_goals_app import views


urlpatterns = [
    
    path('study_goals/',views.Study_goals, name='index')
]
