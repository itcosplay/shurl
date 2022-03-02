from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=500)
    
    short_link = models.CharField(max_length=100)

    def __str__(self):
        return self.link