from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from api.models import File
from django.contrib.auth.models import User
import os
import re
import json


class ViewsTestCase(TestCase):
    """Test suite for views."""

    def setUp(self):
        """setup variables"""
        self.tearDown()
        self.client = APIClient()
        self.user = User.objects.create(username="nerd", password="password")
        self.client.force_authenticate(user=self.user)
        self.client.login(username="nerd", password="password")

        # define the repeated task of post request here
        data = {
            "_file": self.create_file('/tmp/test_file'),
            "owner": self.user.id
        }
        self.response = self.client.post(
            reverse('files-list'),
            data, format="multipart")

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
        return f

    def test_file_upload(self):
        """Test that the user can upload a file."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_getting_all_files(self):
        """Test that the user can get all the files."""

        res = self.client.get(reverse('files-list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data)

    def test_getting_specific_file(self):
        """Test that a user can get a specific file given the id."""

        # get the created file
        the_file = File.objects.get()
        res = self.client.get(
            reverse('files-detail', kwargs={'pk': the_file.id}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, the_file)

    def testing_file_modification(self):
        """Test a user can edit an existing file."""
        the_file = File.objects.get()
        new_file = self.create_file('/tmp/file')
        new_data = {
            "_file": new_file,
            "owner": self.user.id
        }
        res = self.client.put(
            reverse('files-detail', kwargs={'pk': the_file.id}),
            new_data,
            format="multipart"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_deleting_a_file(self):
        """Ensure an existing file can be deleted."""

        new_file = File.objects.get()
        res = self.client.delete(
            reverse('files-detail', kwargs={'pk': new_file.id}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
