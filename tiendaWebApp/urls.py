from django.urls import path
from tiendaWebApp import views


urlpatterns = [
    
    path('',views.home, name="Home"),
    path('store',views.store, name="store"),
    path('more',views.more, name="more"),
    path('contact',views.contact, name="contact")
]