from rest_framework import serializers
from .models import Item, Party, Saved, Googleuser

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'info', 'price', 'stock')

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'creator', 'name', 'info', 'start', 'end', 'theme', 'address', 'longitude', 'lattitude')

class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = ('id_user', 'id_party')



class GoogleuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Googleuser
        fields = ('id',)