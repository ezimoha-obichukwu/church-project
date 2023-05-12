from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    location = models.TextField(blank=True)


    def __str__(self):
        return self.name