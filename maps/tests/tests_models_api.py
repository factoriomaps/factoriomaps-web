from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from maps.models import Map, Mod

class SanityTest(APITestCase):
    fixtures = ['users', 'maps']

    def test_my_sanity(self):
        self.assertTrue('sanity is there')
