from django.db import models


class Link(models.Model):
    url = models.CharField (
        max_length=1000
    )

    short_url = models.CharField (
        blank=True,
        max_length=100
    )

    coustom_url = models.CharField (
        max_length=500,
        blank=True
    )

    def __str__(self):
        return self.url