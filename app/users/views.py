from django.shortcuts import render, redirect, reverse
from .forms import EventForm, ResponseEventUpdateForm, \
    ResponseEventArchiveUpdateForm, EventsArchiveUpdateForm, \
    EventsUpdateForm, LoginUserForm
from events.models import Events, ResponseEvent
from django.views.generic import UpdateView, DetailView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import LoginUserForm, UserRegistrationForm


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('eventer_my_stats'))
    else:
        form = LoginUserForm()

    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def eventer_response(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('eventer_list')
    else:
        form = EventForm()
    context = {
        'form': form,

    }
    return render(request, 'user/eventer_response.html', context)


def eventer_my_stats(request):
    events_response = ResponseEvent.objects.filter(user=request.user).filter(antispam=False)
    events = Events.objects.filter(user=request.user).filter(type_status='Одобрено')
    events_local = Events.objects.filter(user=request.user).filter(type_event='Локальные мероприятия') \
        .filter(type_status='Одобрено')
    events_global = Events.objects.filter(user=request.user).filter(type_event='Глобальные мероприятия') \
        .filter(type_status='Одобрено')

    context = {
        'events_response': events_response,
        'events': events,
        'events_local': events_local,
        'events_global': events_global
    }
    return render(request, 'user/eventer_my_stats.html', context)


def eventer_stats(request):
    events_response = ResponseEvent.objects.filter(antispam=False)
    events = Events.objects.filter(type_status='Одобрено')
    events_local = Events.objects.filter(type_event='Локальные мероприятия').filter(type_status='Одобрено')
    events_global = Events.objects.filter(type_event='Глобальные мероприятия').filter(type_status='Одобрено')
    context = {
        'events_response': events_response,
        'events': events,
        'events_local': events_local,
        'events_global': events_global,
    }
    return render(request, 'user/assist/eventer_stats.html', context)


def eventer_my_response(request):
    my_response = ResponseEvent.objects.filter(user=request.user).filter(antispam=False).filter(archive=False)

    context = {
        'my_response': my_response
    }
    return render(request, 'user/eventer_my_response.html', context)


def eventer_response_faction(request):
    faction = ResponseEvent.objects.filter(user=None).select_related('user')

    context = {
        'faction': faction,
    }
    return render(request, 'user/eventer_response_faction.html', context)


class ResponseFactionUpdateView(UpdateView, DetailView):
    model = ResponseEvent
    template_name = 'user/eventer_response_faction_update.html'
    form_class = ResponseEventUpdateForm
    context_object_name = 'faction'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect('eventer_my_response')


class ResponseFactionArchiveUpdateView(UpdateView, DetailView):
    model = ResponseEvent
    template_name = 'user/eventer_faction_archive_form.html'
    form_class = ResponseEventArchiveUpdateForm
    context_object_name = 'faction'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.archive = True
        self.object.save()
        return redirect('eventer_response_faction_archive')


def eventer_response_faction_archive(request):
    my_response = ResponseEvent.objects.filter(user=request.user).filter(archive=True)

    context = {
        'my_response': my_response
    }
    return render(request, 'user/eventer_response_faction_archive.html', context)


def eventer_list(request):
    my_response = Events.objects.filter(user=request.user).filter(archive=False)

    context = {
        'my_response': my_response,
    }
    return render(request, 'user/eventer_list.html', context)


class EventsArchiveUpdateView(UpdateView, DetailView):
    model = Events
    template_name = 'user/eventer_archive_form.html'
    form_class = EventsArchiveUpdateForm
    context_object_name = 'faction'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.archive = True
        self.object.save()
        return redirect('eventer_response_faction_archive')


def eventer_list_archive(request):
    my_response = Events.objects.filter(user=request.user).filter(archive=True)

    context = {
        'my_response': my_response
    }
    return render(request, 'user/eventer_archive.html', context)


def event_list(request):
    response = Events.objects.filter(type_status='На рассмотрение').filter(archive=False)

    context = {
        'response': response,
    }
    return render(request, 'user/assist/event_list.html', context)


class EventsUpdateView(UpdateView, DetailView):
    model = Events
    template_name = 'user/assist/event_info.html'
    form_class = EventsUpdateForm
    context_object_name = 'faction'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('event_list_assist')
