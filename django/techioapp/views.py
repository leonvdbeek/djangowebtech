from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Item, Party, Saved, Googleuser
from django.shortcuts import redirect
from .forms import Itemform
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer, PartySerializer, SavedSerializer, GoogleuserSerializer
from django.http import Http404
from datetime import date

#unsave view which supports delete only to delete a saved party from saved
class unsaveView(APIView):
    def get_saved(self, userid, partyid):
        try:
            return Saved.objects.get(id_user=userid, id_party=partyid)
        except Party.DoesNotExist:
            raise Http404

    def delete(self, request, userid, partyid, format=None):
        saved = self.get_saved(userid, partyid)
        saved.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Class to Save party to some googleid's saved parties list
class saveView(APIView):
    def post(self, request, format=None):
        serializer = SavedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#Class to add a Google user id
class useridView(APIView):
    def post(self, request, format=None):
        serializer = GoogleuserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#get organized parties when providing a creator id
class organizedView(APIView):
    def get_organized(self, pk):
        try:
            return Party.objects.all().filter(creator=pk)
        except Party.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        parties = self.get_organized(pk)
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

#returns all saved parties of some user id
class savedView(APIView):
    def get_saved(self, pk):
        try:
            return Saved.objects.all().filter(id_user=pk)
        except Saved.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        saved = self.get_saved(pk)
        serializer = SavedSerializer(saved, many=True)
        return Response(serializer.data)

#returns all google user id's
class alluseridView(APIView):
    def get(self, request, format=None):
        userids = Googleuser.objects.all()
        serializer = GoogleuserSerializer(userids, many=True)
        return Response(serializer.data)

#returns a list of all parties starting today
class todayView(APIView):
    def get(self, request, format=None):
        today = date.today()
        partiestoday = Party.objects.filter(start__year=today.year, start__month=today.month, start__day=today.day)
        serializer = PartySerializer(partiestoday, many=True)
        return Response(serializer.data)

#returns a list of all parties starting after moment of request
class futureView(APIView):
    def get(self, request, format=None):
        parties = Party.objects.filter(start__gt=timezone.now())
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

#Lists all the parties sorted by start date and time
class PartyList(APIView):
    def get(self, request, format=None):
        parties = Party.objects.all().order_by('-start')
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PartySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#class to request, update and delete a specific party identified by the party id
class PartyListElement(APIView):
    def get_party(self, pk):
        try:
            return Party.objects.get(pk=pk)
        except Party.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        party = self.get_party(pk)
        serializer = PartySerializer(party)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        party = self.get_party(pk)
        serializer = PartySerializer(party, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        party = self.get_party(pk)
        party.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Not used for PartyFinder app
class ItemList(APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#Not used for PartyFinder app
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

#Not used for PartyFinder app
def item_list(request):
    items = Item.objects.all()
    return render(request, 'techioapp/item_list.php', {'items': items})

#Not used for PartyFinder app
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
    return render(request, 'techioapp/item_new.php', {'form': form})

#Not used for PartyFinder app
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'techioapp/item_detail.php', {'item': item})

#Not used for PartyFinder app
def howdoesitwork(request):
    return render(request, 'techioapp/howdoesitwork.php')

#Not used for PartyFinder app
def shoppingcart(request):
    return render(request, 'techioapp/shoppingcart.php')

#Not used for PartyFinder app
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
    return render(request, 'techioapp/item_edit.php', {'form': form})

#Not used for PartyFinder app
def item_remove(request, pk):
    item = get_object_or_404(Item, pk=pk).delete()
    return HttpResponseRedirect(reverse('item_list'))
