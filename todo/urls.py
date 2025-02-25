from django.urls import path
from .views import home,welcome,task_list,toggle_completion,delete_task

urlpatterns=[
    path('',home,name='home'),
    path('welcome/',welcome,name='welcome'),
    path('tasks/',task_list,name='task_list'),
    path("toggle/<int:task_id>/",toggle_completion,name='toggle_completion'),
    path("delete/<int:task_id>/",delete_task,name='delete_task'),
]