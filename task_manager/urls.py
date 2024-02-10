from django.urls import path
from . import views

app_name = 'task_manager'

urlpatterns = [
    path('', views.home, name="task-list"),
]

htmx_urlpatterns = [
    path('add-task/<int:group_id>/', views.add_task, name='add-task'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
    path('add-group/', views.add_group, name='add-group'),
    path('delete-group/<int:group_id>/', views.delete_group, name='delete-group'),
    path('change-group/<int:group_id>/', views.change_group, name='change-group'),
    path('switch-state/<int:task_id>/', views.switch_task_state, name='switch-task-state'),
    path('sort-group/', views.sort_group, name='sort-group')
]

urlpatterns += htmx_urlpatterns
