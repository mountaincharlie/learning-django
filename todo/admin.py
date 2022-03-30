from django.contrib import admin
from .models import Item  # our class

# Register your models here (in order to see these items in the admin)
admin.site.register(Item)
