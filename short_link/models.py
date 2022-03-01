from django.db import models


class Link(models.Model):
    link = models.TextField()
    
    short_link = models.TextField()

    def __str__(self):
        return self.link