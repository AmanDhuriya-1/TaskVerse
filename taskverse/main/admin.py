from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'desc', 'due_date', 'tags','completed') 

admin.site.register(Task, TaskAdmin)
