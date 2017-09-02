from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from api.models import File
import os
import re


class ViewsTestCase(TestCase):
    """Test suite for views."""

    def setUp(self):
        """setup variables"""
        self.client = APIClient()

    def tearDown(self):
        """clean up residual test files."""
        File.objects.all().delete()
        pattern = "^(?=test_file)\w+"
        if os.path.isdir(os.getcwd() + '/media/files/'):
            for the_file in os.listdir("media/files"):
                # remove all the uploaded test files
                if re.search(pattern, the_file):
                    os.remove(os.getcwd() + '/media/files/' + the_file)

    def create_file(self, filepath):
        """Create a file for testing."""
        f = open(filepath, 'w')
        f.write('this is a good file\n')
        f.close()
        f = open(filepath, 'rb')
        return {'_file': f}

    def test_file_upload(self):
        """Test that the user can upload a file."""

        data = self.create_file('/tmp/test_file')
        response = self.client.post(
            reverse('files-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getting_all_files(self):
        """Test that the user can get all the files."""

        data = self.create_file('/tmp/file')
        response = self.client.post(
            reverse('files-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        res = self.client.get(reverse('files-list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data)

    def test_getting_specific_file(self):
        """Test that a user can get a specific file given the id."""

        data = self.create_file('/tmp/file')
        response = self.client.post(
            reverse('files-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # get the created file
        the_file = File.objects.get()
        res = self.client.get(
            reverse('files-detail', kwargs={'pk': the_file.id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, the_file)

    def test_deleting_a_file(self):
        """Ensure an existing file can be deleted."""
        data = self.create_file('/tmp/file')
        response = self.client.post(
            reverse('files-list'), data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # get the file that's just been uploaded
        new_file = File.objects.get()
        res = self.client.delete(
            reverse('files-detail', kwargs={'pk': new_file.id}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

