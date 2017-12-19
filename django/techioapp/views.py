from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Todo, Item
from django.shortcuts import redirect
from .forms import Todoform



def item_list(request):
    items = Item.objects.all()
    return render(request, 'techioapp/item_list.html', {'items': items})

def item_new(request):
    if request.method == "POST":
        form = Itemform(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = Itemform()
    return render(request, 'techioapp/item_edit.html', {'form': form})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'techioapp/item_detail.html', {'item': item})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = Itemform(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = Itemform(instance=item)
    return render(request, 'techioapp/item_edit.html', {'form': form})









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
