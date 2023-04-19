from django.db import models

class Study_Goal(models.Model):
    study_goal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey('courses_app.Course', on_delete=models.CASCADE)
    due_date = models.DateField()
    details = models.TextField(blank=True)
    manual_progress = models.BooleanField()
    progress = models.IntegerField()
    
    def __str__(self):
        return str(self.study_goal_id)
    
class Study_Goal_Attachment(models.Model):
    attachments_id = models.AutoField(primary_key=True)
    study_goal_id = models.ForeignKey(Study_Goal, on_delete=models.CASCADE)
    file = models.FileField
    
    def __str__(self):
        return str(self.attachments_id)
    
class Related_Task(models.Model):
    related_task_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey('tasks_app.Task', on_delete=models.CASCADE)
    study_goal_id = models.ForeignKey(Study_Goal, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.related_task_id)
    
