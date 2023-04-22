from django.shortcuts import render
from django.http import HttpResponse
from schedule_app.models import Event 

# Create your views here.

def Schedule(request):
    events_list = Event.objects.order_by('date')
    event_dict ={'event': events_list}
    
    return render(request, 'schedule_app/schedule.html', context = event_dict)