from django.db import models

class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    office = models.CharField(max_length=100, blank=True)
    office_details = models.TextField(blank=True)
    
    def __str__(self):
        return self.instructor_id
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6)
    credits = models.IntegerField()
    type = models.CharField(max_length=20)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    ta_info = models.TextField(blank=True)
    details = models.TextField(blank=True)
    
    def __str__(self):
        return self.course_id
    
class Course_Meeting(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    day = models.CharField(max_length=15)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return self.meeting_id
    
class Course_Attachment(models.Model):
    attachments_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    file = models.FileField()
    
    def __str__(self):
        return self.attachments_id
