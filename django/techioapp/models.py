from django.db import models
from django.utils import timezone
from django.utils.encoding import force_unicode
import os.path

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



class RenameFilesModel(models.Model):
    RENAME_FILES = {}

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False):
        rename_files = getattr(self, 'RENAME_FILES', None)
        if rename_files:
            super(RenameFilesModel, self).save(force_insert, force_update)
            force_insert, force_update = False, True

            for field_name, options in rename_files.iteritems():
                field = getattr(self, field_name)
                file_name = force_unicode(field)
                name, ext = os.path.splitext(file_name)
                keep_ext = options.get('keep_ext', True)
                final_dest = options['dest']
                if callable(final_dest):
                    final_name = final_dest(self, file_name)
                else:
                    final_name = os.path.join(final_dest, '%s' % (self.pk,))
                    if keep_ext:
                        final_name += ext
                if file_name != final_name:
                    field.storage.delete(final_name)
                    field.storage.save(final_name, field)
                    field.storage.delete(file_name)
                    setattr(self, field_name, final_name)

        super(RenameFilesModel, self).save(force_insert, force_update)

class Item(RenameFilesModel):
    name = models.CharField(max_length=20)
    info = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    file = models.ImageField(upload_to='djangowebtech/django/techioapp/static/temp')

    def bought(self):
        self.stock = self.stock-1
        self.save()

    def __str__(self):
        return self.name

    RENAME_FILES = {
        'file': {'dest': 'djangowebtech/django/techioapp/static/img', 'keep_ext': True}
    }
