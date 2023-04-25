from django import forms
from django.forms import ModelForm
from schedule_app.models import Event
from django.utils.translation import gettext_lazy as _
from core_app.models import Semester

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["event_id","semester_id","title","date","start_time", "end_time", "notes"]
        labels = {
            "event_id":_("Event"),
            "semester_id":_("Semester"),
            "title":_("Title"),
            "date":_("Date"),
            "start_time":_("Start Time"),
            "end_time":_("End Time"),
            "notes":_("Notes"),
        }