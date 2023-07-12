from django.db import models

class Committee(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    contact = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.name}"
