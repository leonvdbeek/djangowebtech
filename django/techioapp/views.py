from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Todo

def todo_list(request):
    todos = Todo.objects.order_by('completed_date')
    return render(request, 'techioapp/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'techioapp/todo_detail.html', {'todo': todo})

def todo_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.deadline_date = timezone.now()
            todo.save()
            return redirect('post_detail', pk=todo.pk)
    else:
        form = PostForm()
    return render(request, 'techioapp/todo_edit.html', {'form': form})
