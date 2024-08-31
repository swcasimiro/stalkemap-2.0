from django.shortcuts import render, redirect
from .forms import ResponseEventForm
from locations.models import Location
from .models import Events
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


async def event_response(request):
    location = Location.objects.all()
    if request.method == "POST":
        form = ResponseEventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.user = request.user
            post.save()
            return redirect('event_success')
    else:
        form = ResponseEventForm()
    context = {
        'form': form,
        'location': location
    }
    return render(request, 'events/event_response.html', context)


async def event_success(request):
    location = Location.objects.all()
    context = {
        'location': location
    }
    return render(request, 'events/event_success.html', context)


async def event_global(request):
    location = Location.objects.all()
    events = (Events.objects.filter(type_event='Глобальные мероприятия').filter(type_status='Одобрено')
              .values('name', 'description', 'type_event', 'vk'))
    context = {
        'status_event': 'Глобальные мероприятия',
        'location': location,
        'events': events
    }
    return render(request, 'events/event_list.html', context)


async def event_local(request):
    location = Location.objects.all()
    events = (Events.objects.filter(type_event='Локальные мероприятия').filter(type_status='Одобрено')
              .values('name', 'description', 'type_event', 'vk'))
    context = {
        'status_event': 'Локальные мероприятия',
        'location': location,
        'events': events
    }
    return render(request, 'events/event_list.html', context)
