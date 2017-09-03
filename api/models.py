"""
This file represents the models for the api app.
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .utils import generate_uid
import os


class DateMixin(models.Model):
    """A model mixin for date creation."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class File(DateMixin):
    """This class represents the file model."""

    file_id = models.CharField(default=generate_uid, max_length=20)
    _file = models.FileField(upload_to="files")
    owner = models.ForeignKey(
        User, related_name="files", on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.file_id)


@receiver(post_delete, sender=File)
def delete_file(sender, instance, **kwargs):
    """
    This function deletes the associated file
    from the file storage when it's instance is deleted
    from the database
    """
    file_path = instance._file.path
    if os.path.exists(file_path):
        os.remove(file_path)


@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    """
    This function handles a signal to create an auth token immediately a user
    created
    """
    if created:
        Token.objects.create(user=instance)
