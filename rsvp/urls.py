from django.urls import path
from . import views

app_name = 'rsvp'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('<slug:slug>/', views.landing_page, name='guest_landing'),
]
