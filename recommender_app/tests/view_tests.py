from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client


# Create your tests here.
class PredictionTest(TestCase):

    def setUp(self):
        self.pre_http = "http://127.0.0.1:8000"
        self.client = Client()

    def test_prediction(self):
        response = self.client.post(self.pre_http + reverse('predict-artist'), data={'artist-name': 'die Ärzte'})
        print(response.content)
