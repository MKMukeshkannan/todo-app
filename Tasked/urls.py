from django.contrib import admin
from django.urls import path
from todo.views import home as todo_homne
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_homne, name = 'home')
]
