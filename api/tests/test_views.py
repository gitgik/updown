from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ViewsTestCase(TestCase):
    """Test suite for views."""

    def setUp(self):
        """setup variables"""
        self.client = APIClient()

    def create_file(self, filepath):
        """Create a file for testing."""
        f = open(filepath, 'w')
        f.write('this is a good file\n')
        f.close()
        f = open(filepath, 'rb')
        return {'_file': f}

    def test_file_upload(self):
        data = self.create_file('/tmp/file')
        response = self.client.post(
            reverse('api.upload'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getting_all_files(self):
        response = self.client.get(reverse('file_get'))

    def test_getting_specific_file(self):
        pass

    def test_deleting_a_file(self):
        """Ensure an existing file can be deleted."""
        data = self.create_file('/tmp/file')
        response = self.client.post(
            reverse('api.upload'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # get the file that's just been uploaded
        new_file = File.objects.get()
        res = self.client.delete(
            reverse('api.delete'), kwargs={'pk': new_file.id}, follow=True)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

