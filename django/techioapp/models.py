from django.db import models
from django.utils import timezone



class Item(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    upload = models.ImageField(upload_to='djangowebtech/django/techioapp/static/img')

    def bought(self):
        self.stock = self.stock-1
        self.save()

    def __str__(self):
        return self.name
