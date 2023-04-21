from django import forms
from django.forms import ModelForm
from tasks_app.models import Task, Task_Attachment
from django.utils.translation import gettext_lazy as _

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [ "semester_id", "title", "category", "due_date", "details", "is_complete", "is_pinned" ]
        labels = {
            "semester_id": _("Semester"),
            "category": _("Course"),
            "due_date": _("Due Date"),
            "is_complete": _("Completed?"),
            "is_pinned": _("Pinned?"),
        }