from django.urls import path
from schedule_app import views


urlpatterns = [
    
    path('view_events/',views.events, name='view schedule')
]
