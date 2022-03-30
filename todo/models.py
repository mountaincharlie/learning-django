from django.db import models

# Create your models here (models = our db design/layout)
# class => django creates a table after migrations


class Item(models.Model):  # inheriting Django's base Model class
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # redefining how our items will be named in the db
    def __str__(self):
        return self.name
