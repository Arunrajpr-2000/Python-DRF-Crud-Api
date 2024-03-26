from django.contrib import admin

# Register your models here.
from .models import Item, Location,Tag

admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Tag)