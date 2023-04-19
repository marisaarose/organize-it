from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey('core_app.Semester', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.event_id
