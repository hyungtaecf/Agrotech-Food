from .models import *
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, View

# Displaying gallery images each time in the Index Page
displayingItemsNumber = 7 # IMPORTANT: Should be the same as in gallery.js

class GalleryView(ListView):
    model=GalleryImage
    context_object_name = 'gallery'
    template_name='gallery/gallery.html'

class RetrieveImages(View):
    def get(self, request):
        # Gets via ajax the requested indexes expressed in javascript
        fromIndex = int(request.GET.get('fromIndex', None))
        toIndex = int(request.GET.get('toIndex', None))

        # Checking pagination position
        first_page = False
        last_page = False
        if fromIndex > GalleryImage.objects.all().count()-1: # Is it going to the First Page?
            first_page = True
            fromIndex = 0
            toIndex = displayingItemsNumber
        elif fromIndex < 0: # Is it going to the Last Page?
            last_page = True
            fromIndex = (GalleryImage.objects.all().count() -
                GalleryImage.objects.all().count()%displayingItemsNumber)
            toIndex = GalleryImage.objects.all().count()

        if toIndex > GalleryImage.objects.all().count(): # Is it the Last Page and not full?
            toIndex = GalleryImage.objects.all().count()

        slicedListOfImages = serializers.serialize("json",GalleryImage.objects.all().order_by('id')[fromIndex:toIndex])
        data = {
            'slicedListOfImages': slicedListOfImages,
            'fromIndex': fromIndex,
            'toIndex': toIndex,
        }
        return JsonResponse(data)
