from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client
import json


# Create your tests here.
class PredictionTest(TestCase):

    def setUp(self):
        self.pre_http = "http://127.0.0.1:8000"
        self.client = Client()

    def test_prediction(self):
        number = 5
        response = self.client.post(self.pre_http + reverse('predict-artist'), data={'artist-name': 'die Ärzte',
                                                                                     'number': number})
        recommendations = json.loads(response.content)['recommendations']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(recommendations), number)

    def test_prediction_incomplete_parameters(self):
        response = self.client.post(self.pre_http + reverse('predict-artist'), data={})
        self.assertEqual(response.status_code, 400)

    def test_prediction_not_valid_number(self):
        number = 'e'
        response = self.client.post(self.pre_http + reverse('predict-artist'), data={'artist-name': 'die Ärzte',
                                                                                     'number': number})
        self.assertEqual(response.status_code, 400)
        print(response.content)
