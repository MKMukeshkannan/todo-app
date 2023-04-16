from django.contrib import admin
from django.urls import path
from todo.views import home as todoHome
from todo.views import todoMain as todoList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoHome, name = 'home'),
    path('todo/',todoList, name = 'todo'),

]
