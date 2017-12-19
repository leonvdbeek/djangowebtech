from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Todo, Item
from django.shortcuts import redirect
from .forms import Todoform


def todo_list(request):
    todos = Todo.objects.order_by('completed_date')
    return render(request, 'techioapp/todo_list.html', {'todos': todos})

def item_list(request):
    items = Item.objects
    return render(request, 'techioapp/item_list.html', {'items': items})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'techioapp/todo_detail.html', {'todo': todo})

def todo_new(request):
    if request.method == "POST":
        form = Todoform(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = Todoform()
    return render(request, 'techioapp/todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = Todoform(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = Todoform(instance=todo)
    return render(request, 'techioapp/todo_edit.html', {'form': form})
