from django.contrib import admin
from tasks_app.models import Task, Task_Attachment
from core_app.models import Semester
from courses_app.models import Course, Instructor

admin.site.register(Task)
admin.site.register(Task_Attachment)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Instructor)