import os
from time import time
from hashids import Hashids
from django.conf import settings


def generate_uid(salt=settings.SECRET_KEY):
    """
    Generate a unique identifier for the File name.
    """
    min_length = 20
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    hashids = Hashids(salt=salt, min_length=min_length, alphabet=alphabet)
    uid = hashids.encode(int(time() * 1000))
    return uid


def get_file_upload_path(instance, filename):
    """
    This function is called to obtain the upload path
    (relative to MEDIA_ROOT) including the filename for
    the file to be saved to disk.
    """
    name, ext = os.path.splitext(filename)
    new_filename = "{}{}".format(instance.file_id, ext)

    upload_path = "files/{}".format(new_filename)
    return upload_path
