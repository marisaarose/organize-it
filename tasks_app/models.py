from django.db import models
from django.forms import ModelForm
from django import forms
from core_app.models import Semester
import os

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey('core_app.Semester', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey('courses_app.Course', on_delete=models.CASCADE)
    due_date = models.DateField()
    details = models.TextField(blank=True)
    is_complete = models.BooleanField()
    is_pinned = models.BooleanField()
    
    def __str__(self):
        return self.title

class Task_Attachment(models.Model):
    attachments_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField()
    
    def __str__(self):
        return self.attachments_id
    
