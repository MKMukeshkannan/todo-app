from django.shortcuts import render
from .models import todoDB

def home(request):
    return render(request, 'todo/index.html')

def todoMain(request):
    data = todoDB.objects.all()
    context = {
        'data':data,
    }    
    return render(request, 'todo/todo.html', context=context)

