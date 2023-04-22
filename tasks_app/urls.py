from django.urls import path
from tasks_app import views

urlpatterns = [
    path('view-tasks/', views.view_tasks, name='view tasks'),
    path('new-task/', views.new_task, name='new task'),
    path('task-details/<int:id>', views.get_task, name='task details'),
    path('edit-task/<int:id>', views.edit_task, name='edit task'),
    path('new-attachment/<int:id>', views.new_attachment, name='new attachment'),
    path('delete-attachment/<int:id>', views.delete_attachment, name='delete attachment'),
]