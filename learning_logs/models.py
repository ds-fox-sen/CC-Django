"""
Django models.

A Django project is organized as a group of individual apps that work together
to make the project work as a whole. For now, we’ll create just one app to
do most of the work for our project.
"""

from django.db import models


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
