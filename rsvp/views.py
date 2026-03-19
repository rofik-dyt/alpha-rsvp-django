from django.shortcuts import render, get_object_or_404
from .models import Guest


def landing_page(request, slug=None):
    guest = None
    if slug:
        guest = get_object_or_404(Guest, slug=slug)
    return render(request, 'rsvp/landing.html', {'guest': guest})
