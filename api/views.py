from rest_framework import generics

from .models import Item,Location,Tag,Source

from .serializers import ItemSerializer,LocationSerializer,TagSerializer,SourceSerializer


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        location = self.request.query_params.get('location')
        source=self.request.query_params.get('source')
        queryset = Item.objects.all()
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        elif source is not None:
            queryset = queryset.filter(source=source)
        return queryset

    

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=LocationSerializer
    queryset = Location.objects.all()    


class TagList(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= TagSerializer
    queryset = Tag.objects.all()    

class SourceList(generics.ListCreateAPIView):
    serializer_class=SourceSerializer
    queryset = Source.objects.all()

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=SourceSerializer
    queryset = Source.objects.all()    

    



               