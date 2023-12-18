from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    description = models.TextField(blank=True) 

    def __str__(self):
        return f"{self.title}"
