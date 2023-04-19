from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user_id
    
class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    current = models.BooleanField()
    
    def __str__(self):
        return self.semester_id

class Holiday(models.Model):
    holiday_id = models.AutoField(primary_key=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.holiday_id