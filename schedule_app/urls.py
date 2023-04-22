from django.urls import path
from schedule_app import views


urlpatterns = [
    
    path('',views.Schedule, name='view schedule')
]
