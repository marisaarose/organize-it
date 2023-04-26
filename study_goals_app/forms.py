from django .forms import ModelForm
from study_goals_app.models import Study_Goal, Study_Goal_Attachment, Related_Task

class Study_GoalsForm(ModelForm):
    class Meta:
        model = Study_Goal
        fields = __all__
        
        labels = {
            "event_id": _("event"),
            "semester_id":_("semester"),
            "title": _("title"),
            "date": _("date"),
            "start_time":_("start Time"),
            "end_time": _("end time"),
            "notes": _("notes"),
        }
        
class Study_Goal_AttachmentForm(ModelForm):
    class Meta:
        model = Study_Goal_Attachment
        fields = ["study_goal_id", "file"]
        labels = {
            "study_goal_id":_("Study Goal"),
            "file":_("file"),
        }
class Related_TaskForm(ModelForm):
    class Meta:
        model = Related_Task
        fields = ["task_id", "study_goal_id"]
        labels = {
            "task_id":_("Task"),
            "study_goal_id": _("Study Goal"),
        }