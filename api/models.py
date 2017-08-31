"""
This file represents the models for the api app.
"""
from django.db import models


class DateMixin(models.Model):
    """A model mixin for date creation."""

    created = models.DateField(auto_now_add=True)


class File(DateMixin):
    """This class represents the file model."""

    name = models.CharField(max_length=100, unique=True)
    file = models.FileField(allow_files=True)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.name)

