from django.shortcuts import render, get_object_or_404
from .models import Location, Hood
from events.models import Events
from django.db.models import Q
import time
import trio
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

location_2 = Location.objects.all()


async def index(request):
    location = Location.objects.all()

    context = {
        'location': location,

    }
    return render(request, 'index.html', context)


async def location_list(request, slug):
    location = Location.objects.values('slug', 'name', 'image', 'type')
    location_detail = Location.objects.get(slug=slug)
    cat = get_object_or_404(Location, slug=slug)
    hood = Hood.objects.filter(location=cat).select_related('location')
    context = {
        'location': location,
        'menu': cat,
        'location_detail': location_detail,
        'hood': hood
    }
    return render(request, 'locations/location.html', context)


async def location_detail(request, slug, hood_slug=None):
    hood = Hood.objects.select_related('location').get(slug=hood_slug)
    cat = get_object_or_404(Location, slug=slug)
    context = {
        'hood': hood,
        'menu': cat,
        'location': location_2,
    }

    return render(request, 'locations/location_detail.html', context)
