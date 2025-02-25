from django.contrib import admin

# Register your models here.
from .models import Task #import the Task model
admin.site.register(Task) #Register Task model in admin