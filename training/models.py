from django.db import models

class Training(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    address = models.CharField(max_length=500, blank=True)
    time = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name}"
