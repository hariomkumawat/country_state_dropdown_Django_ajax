from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .form import PersonCreationForm
from .models import *


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'index.html', {'form': form})


# AJAX
def load_state(request):
    country_id = request.GET.get('country_id')
    state = State.objects.filter(country_id=country_id).all()
    return render(request, 'state.html', {'state': state})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'index.html', {'form': form})

