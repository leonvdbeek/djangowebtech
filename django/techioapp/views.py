from django.shortcuts import render
from django.utils import timezone
from .models import todo

def post_list(request):
    posts = todo.objects.filter(completed_date__lte=timezone.now()).order_by('completed_date')
    return render(request, 'techioapp/post_list.html', {'posts': posts})
