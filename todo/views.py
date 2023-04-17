from django.shortcuts import render, redirect
from .models import todoDB
from user.models import User
from .forms import todoForm

def home(request):
    return render(request, 'todo/index.html')

def todoMain(request):
    if request.method == 'POST':
        form = todoForm(request.POST)
        if form.is_valid():
            user = User.objects.all().first()
            todoDB.objects.create(user = user, taskDesc = form.cleaned_data['Task'])
            return redirect('todo')
    else:
        form = todoForm()
    
    data = todoDB.objects.all()
    context = {
        'data':data,
        'form':form,
    }    
    return render(request, 'todo/todo.html', context=context)

def todoDelete(request, pk):
    task = todoDB.objects.get(id=pk)
    task.delete()
    return redirect('todo')

def todoDone(request, pk):
    task = todoDB.objects.get(id=pk)
    if task.status == False:
        task.status = True
    else:
        task.status = False

    task.save()
    return redirect('todo')