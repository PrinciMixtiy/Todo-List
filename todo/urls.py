from django.contrib import admin
from django.urls import path, include

from task_manager import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', include('task_manager.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
