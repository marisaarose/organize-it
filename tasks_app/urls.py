from django.urls import path
from tasks_app import views

urlpatterns = [
    path('view-tasks/', views.view_tasks, name='view tasks'),
    path('new-task/', views.get_task, name='new task'),
]