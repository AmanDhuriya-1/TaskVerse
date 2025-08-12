from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task, name='task'),              
    path('add/', views.add, name='add'),           
    path('edit/<int:id>/', views.edit, name='edit'), 
    path('delete/<int:id>/', views.delete, name='delete'), 
    path('history/', views.history, name='history'),
    path('toggle/<int:id>/', views.toggle_complete, name='toggle_complete'), 
    path('restore-task/<int:log_id>/', views.restore_task, name='restore_task'),
    path('delete-log/<int:log_id>/', views.delete_log, name='delete_log'),
    path('logout/', views.logout_view, name='logout'),
]
