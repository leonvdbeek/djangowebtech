from django import forms

from .models import Todo, Item

class Todoform(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'text',)

class Itemform(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'info', 'price', 'stock', 'file')
