from django.shortcuts import render, HttpResponse
from services_app.models import Services 

# Create your views here.
def home(request):
    return render(request, "proyecto_web_app/home.html")


def services(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, "proyecto_web_app/services.html", context)


def store(request):
    return render(request, "proyecto_web_app/store.html")


def blog(request):
    return render(request, "proyecto_web_app/blog.html")


def contact(request):
    return render(request, "proyecto_web_app/contact.html")


