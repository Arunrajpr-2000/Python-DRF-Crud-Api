from django.urls import path
from .views import ItemList, ItemDetail,LocationList,LocationDetail,TagList,TagDetail

urlpatterns = [
  path('item/',ItemList.as_view()),
  path('item/<int:pk>/',ItemDetail.as_view()),
  path('location/',LocationList.as_view()),
  path('location/<int:pk>/',LocationDetail.as_view()),
  path('tag/',TagList.as_view()),
  path('tag/<int:pk>/',TagDetail.as_view())
]