"""organize_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks_app import views
from django.conf.urls import include
from schedule_app import views
from study_goals_app import views 
urlpatterns = [ path('schedule_app/', include('schedule_app.urls')),
    path('study_goals_app/', include('study_goals_app.urls')),
    path('tasks_app/', include('tasks_app.urls')),
    path('admin/', admin.site.urls),
]
