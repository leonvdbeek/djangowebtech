from django.shortcuts import render
from django.utils import timezone
from .models import todo

def todo_list(request):
    todos = todo.objects.order_by('completed_date')
    return render(request, 'techioapp/todo_list.html', {'todos': todos})
