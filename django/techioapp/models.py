from django.db import models
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    deadline_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def complete(self):
        self.completed_date = timezone.now()
        self.completed = True
        self.save()

    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=20)
    info = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    upload = models.ImageField(upload_to='djangowebtech/django/techioapp/static/img', default = 'pic_folder/None/no-img.jpg')

    def bought(self):
        self.stock = self.stock-1
        self.save()

    def __str__(self):
        return self.name
