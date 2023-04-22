from django.urls import path
from schedule_app import views


urlpatterns = [
    
    path('view-schedule/',views.Schedule, name='view schedule')
]
