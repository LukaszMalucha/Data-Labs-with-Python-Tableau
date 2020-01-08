from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

TEST_PROFILE_URL = reverse("api:test-profile")


class TestProfileViewTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_test_profile_view(self):
        """Test get method"""
        response = self.client.get(TEST_PROFILE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_valid_dataskills(self):
        """Test evaluating skillset"""
        payload = {'skills': "Agile, Analytics"}
        response = self.client.post(TEST_PROFILE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_empty_dataskills(self):
        """Test evaluating skillset"""
        payload = {'skills': ""}
        response = self.client.post(TEST_PROFILE_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
