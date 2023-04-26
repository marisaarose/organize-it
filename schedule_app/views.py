from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect 
from schedule_app.models import Event 

# Create your views here.

def view_schedule(request):
    schedule_list = Event.objects.order_by('Date')
    schedule_dict ={'event': schedule_list}
    return HttpResponse("I'm HERE")
    
    return render(request, 'schedule_app/view-schedule.html', context = {'event':schedule_dict})

def new_event(request):
    context = {}
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            event = Event.objects.latest('event_id')
            return redirect('event details', Event.event_id)
    else:
        form = EventForm()
    context['form'] = form
    return render(request, "schedule_app/new-event.html", context)

def edit_event(request, id):
    event = Event.objects.get(task_id = id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, isinstance=event)
        if form.is_valid():
            if form.instance.is_complete == True:
                form.instance.is_pinned = False
            form.save()
            return redirect('event details', event.event_id)
    else:
        form = EventForm(instance=event)
        
    return render(request, 'schedule_app/edit-event.html', context = {'form': form,})


def delete_event(request, id):
    event = Event.objects.get(task_id = id)
    event.delete()
    
    return redirect("view event")