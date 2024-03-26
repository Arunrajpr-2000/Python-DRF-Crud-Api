from django.contrib import admin

# Register your models here.
from .models import Item, Location,Tag,Source

admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Tag)
admin.site.register(Source)