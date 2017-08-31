from django.test import TestCase
from api.models import File, DateMixin
from django.core.files.uploadedfile import SimpleUploadedFile


class ModelsTestCase(TestCase):
    """Test suite for the models."""

    def setUp(self):
        """Setup variables."""
        self.file_object = File()
        self.dates = DateMixin()

    def test_file_creation(self):
        """Test whether a book can be created."""
        self.file_object._file = SimpleUploadedFile(
            name='test_file.jpeg',
            content=open('/tests/test_file.jpeg', 'rb').read(),
            content_type='image/jpeg')
        self.file_object.save()
        self.assertIsInstance(self.file_object, File)
        self.assertEqual(File.objects.count(), 1)

    def test_date_mixin(self):
        """Test the date mixin works."""
        self.assertIsInstance(self.dates, DateMixin)

    def test_models__human_readable_representation(self):
        """Test the models instances return a string."""
        self.assertTrue(str(self.file_object))
