from django.db import models


class Link(models.Model):
    url = models.CharField(
        max_length=500,
        unique=True
    )
    
    short_url = models.CharField(max_length=100)

    def __str__(self):
        return self.url