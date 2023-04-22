from django.db import models

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    office = models.CharField(max_length=255, blank=True)
    office_details = models.TextField(blank=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=6)
    credits = models.IntegerField()
    TYPE_CHOICES = (
        ('in-person', 'In Person'),
        ('online', 'Online')
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    ta_info = models.TextField(blank=True)
    details = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Course_Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, blank=True)
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    )
    day = models.CharField(max_length=15, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return str(self.meeting_id)
    
class Course_Attachment(models.Model):
    attachments_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField()
    
    def __str__(self):
        return str(self.attachments_id)
