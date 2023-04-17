from django.shortcuts import render
from .models import todoDB
from .forms import todoForm

def home(request):
    return render(request, 'todo/index.html')

def todoMain(request):
    data = todoDB.objects.all()
    context = {
        'data':data,
        'form':todoForm,
    }    
    return render(request, 'todo/todo.html', context=context)

