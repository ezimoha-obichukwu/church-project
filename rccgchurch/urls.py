from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('volunteer/', views.volunteer_page, name="volunteer"),
    path('contact/', views.contact_page, name="contact"),
    path('connect-group/', views.connect_group_page, name="connect-group"),
    path('events/', views.event_page, name="event"),
    path('events-single/', views.event_single_page, name="event-single")
]