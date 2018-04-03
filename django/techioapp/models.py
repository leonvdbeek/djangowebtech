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

class Party(models.Model):
    creator = models.ForeignKey('Googleuser', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    info = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    theme = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Googleuser(models.Model):
    id=models.CharField(primary_key=True, max_length=21, unique=True)
    #name=models.CharField(max_length=20, default='0')

    def __str__(self):
        return self.id

class Saved(models.Model):
    id_user = models.ForeignKey('Googleuser', on_delete=models.CASCADE)
    id_party = models.ForeignKey('Party', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('id_user', 'id_party',)

    def __str__(self):
        return (self.id_party.name + "  saved by  " + self.id_user.id)





