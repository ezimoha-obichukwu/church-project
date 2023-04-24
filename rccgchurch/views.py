from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def event_page(request):
    return render(request, "events.html")

def event_single_page(request):
    return render(request, "events-single.html")

def contact_page(request):
    return render(request, "contact.html")

def connect_group_page(request):
    return render(request, "connect-group.html")

def volunteer_page(request):
    return render(request, "volunteer.html")