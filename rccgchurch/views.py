from django.shortcuts import render
from .models import Event

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def event_page(request):
    events = Event.objects.all()
    context = {
        "all_events": events
    }
    return render(request, "events.html", context)

def event_single_page(request):
    return render(request, "events-single.html")

def contact_page(request):
    return render(request, "contact.html")

def connect_group_page(request):
    return render(request, "connect-group.html")

def volunteer_page(request):
    return render(request, "volunteer.html")