from django.test import TestCase
from api.models import File, DateMixin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import os
import re


class ModelsTestCase(TestCase):
    """Test suite for the models."""

    def setUp(self):
        """Setup variables."""
        self.file_object = File()
        self.dates = DateMixin()
        self.test_file_path = os.getcwd() + "/api/tests/test_file.jpeg"
        self.user = User.objects.create(username="test_user")

    def tearDown(self):
        """Remove files after testing."""
        File.objects.all().delete()
        pattern = "^(?=test_file)\w+"
        if os.path.isdir(os.getcwd() + '/media/files/'):
            for the_file in os.listdir("media/files"):
                # remove all the uploaded test files
                if re.search(pattern, the_file):
                    os.remove(os.getcwd() + '/media/files/' + the_file)

    def test_model_can_create_file(self):
        """Test whether a file can be created using the model."""
        with open(self.test_file_path, 'rb') as f:
            jpg_data = f.read()
        self.file_object._file = SimpleUploadedFile(
            name="test_file.jpeg",
            content=jpg_data,
            content_type='image/jpeg')
        self.file_object.owner = self.user
        self.file_object.save()
        self.assertIsInstance(self.file_object, File)
        self.assertEqual(File.objects.count(), 1)

    def test_date_mixin(self):
        """Test the date mixin works."""
        self.assertIsInstance(self.dates, DateMixin)

    def test_models__human_readable_representation(self):
        """Test the models instances return a string."""
        self.assertTrue(str(self.file_object))
