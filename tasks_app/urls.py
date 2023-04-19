from django.urls import path
from tasks_app import views

urlpatterns = [
    path('', views.view_tasks, name='view tasks'),
]