from django.contrib import admin
from django.urls import path
from todo.views import home as todoHome
from todo.views import todoMain as todoList
from todo.views import todoDelete, todoDone
from django.contrib.auth import views as authViews
from user.views import customUserCreation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoHome, name = 'home'),
    path('todo/',todoList, name = 'todo'),
    path('<int:pk>/delete', todoDelete, name = 'todoDelete'),
    path('<int:pk>/done', todoDone, name = 'todoDone'),
    path('login/',authViews.LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    path('logout/',authViews.LogoutView.as_view(template_name = 'todo/index.html'), name = 'logout'),
    path('signup/', customUserCreation.as_view(), name = 'signup')
]
