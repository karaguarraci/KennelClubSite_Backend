from django.db import models

class Photo(models.Model):
    title = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='default.png')

    def __str__(self):
        return f"{self.title}"
