from django.db import models


class Link(models.Model):
    url = models.CharField (
        max_length=1000,
        unique=True
    )

    short_url = models.CharField (
        max_length=100,
        unique=True,
        blank=True
    )

    coustom_url = models.CharField (
        max_length=500,
        unique=True,
        blank=True
    )

    def __str__(self):
        return self.url