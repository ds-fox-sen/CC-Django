"""
Django models.

A Django project is organized as a group of individual apps that work together
to make the project work as a whole. For now, we’ll create just one app to
do most of the work for our project.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Tell Django to use Entries when it references more than 1 entry."""

        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string respresentation of the model."""
        return self.text[:50] + "..."
