from rest_framework import serializers
from .models import Item, Location, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')
               

class ItemSerializer(serializers.ModelSerializer):
    
    tags = serializers.SlugRelatedField(slug_field='id',queryset=Tag.objects.all(), many=True) # only id will added to list
    tagDetails = TagSerializer(many=True,source='tags', read_only=True)  # Use TagSerializer to serialize all data in Tag model to Itemseializer

    class Meta:
        model = Item
        fields = ('id', 'itemName', 'date_added', 'itemLocation', 'itemWeight', 'isInside', 'tags','tagDetails')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')
