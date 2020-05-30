from django.db import models


class Room(models.Model):
    """ chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Return the name."""
        return self.name
