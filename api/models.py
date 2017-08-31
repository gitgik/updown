"""
This file represents the models for the api app.
"""
from django.db import models
from .utils import get_file_upload_path, generate_uid


class DateMixin(models.Model):
    """A model mixin for date creation."""

    created = models.DateField(auto_now_add=True)


class File(DateMixin):
    """This class represents the file model."""

    file_id = models.CharField(default=generate_uid, max_length=50)
    _file = models.FileField(upload_to=get_file_upload_path)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.file_id)

