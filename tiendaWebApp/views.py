from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "tiendaWebApp/home.html")

def store(request):
    
    return render(request, "tiendaWebApp/store.html")

def more(request):
    return render(request, "tiendaWebApp/more.html")


def contact(request):
    return render(request, "tiendaWebApp/contact.html")