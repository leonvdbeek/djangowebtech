from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item
from django.shortcuts import redirect
from .forms import Itemform
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer

class ItemList(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def item_list(request):
    items = Item.objects.all()
    return render(request, 'techioapp/item_list.html', {'items': items})


def item_new(request):
    if request.method == "POST":
        form = Itemform(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.upload = request.FILES['upload']
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = Itemform()
    return render(request, 'techioapp/item_new.html', {'form': form})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'techioapp/item_detail.html', {'item': item})

def howdoesitwork(request):
    return render(request, 'techioapp/howdoesitwork.html')

def shoppingcart(request):
    return render(request, 'techioapp/shoppingcart.html')

def item_edit(request):
    if request.method == "POST":
        form = Itemform(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.upload = request.FILES['upload']
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = Itemform()
    return render(request, 'techioapp/item_edit.html', {'form': form})

def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk).delete()
    return HttpResponseRedirect(reverse('item_list'))
