from django.contrib import admin
from django.urls import path
from todo.views import home as todoHome
from todo.views import todoMain as todoList
from todo.views import todoDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoHome, name = 'home'),
    path('todo/',todoList, name = 'todo'),
    path('<int:pk>/delete', todoDelete, name = 'todoDelete')
]
