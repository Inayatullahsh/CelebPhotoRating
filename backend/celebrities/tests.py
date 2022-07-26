from django.contrib.auth import get_user_model

from django.test import TestCase

from rest_framework.test import APITestCase


from .models import Celebrity, Photo, Rating

# Create your tests here.


class CelebrityTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="john", email="john@email.com", password="secret"
        )
        cls.celebrity = Celebrity.objects.create(
            full_name="testuser", created_by=cls.user
        )

    def test_celebrity_model(self):
        self.assertEqual(self.celebrity.full_name, "testuser")
        self.assertEqual(self.celebrity.created_by, self.user)


# Create tests for Photo, and Rating models
