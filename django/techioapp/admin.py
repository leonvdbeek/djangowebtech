from django.contrib import admin
from .models import Item, Party, Googleuser, Saved

# Register your models here.

admin.site.register(Item)
admin.site.register(Party)
admin.site.register(Googleuser)
admin.site.register(Saved)
