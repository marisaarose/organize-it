from django.urls import path
from study_goals_app import views


urlpatterns = [
    
    path('study-goals/',views.Study_goals, name='index'),
    path('edit-goals/',views.edit_study_goals, name='edit goals'),
    path('new-study-goal',views.new_study_goals, name='new goals'),
    path('goals-details/<int:id>',views.get_goal, name='goal details'),
    path('delete-study-goals/<int:id>',views.delete_study_goal, name ='delete goals'),
    
]
