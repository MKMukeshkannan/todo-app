from django.shortcuts import render, reverse
from todo.models import User
from django.views import generic
from user.forms import customUserCreationForm

class customUserCreation(generic.CreateView):
    template_name = 'user/signup.html'
    form_class = customUserCreationForm

    def get_success_url(self):
        return reverse('login')