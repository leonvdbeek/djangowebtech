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
from django.http import Http404

class ItemList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ItemListElement(APIView):
    def get_item(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_item(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_item(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
