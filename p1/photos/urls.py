from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('photos/<int:pk>/',views.viewPhoto,name='photo'),
    path('add/',views.addphoto,name='add')
]
