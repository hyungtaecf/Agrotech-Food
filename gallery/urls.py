from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('', GalleryView.as_view(), name='index'),
    path('ajax/retrieve', RetrieveImages.as_view(), name='ajax_retrieve'),
]
