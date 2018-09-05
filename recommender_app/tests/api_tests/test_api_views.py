from rest_framework.test import APITestCase, RequestsClient
from django.urls import reverse
import json


class RecommenderApiViewTest(APITestCase):

    def setUp(self):
        self.client = RequestsClient()
        self.pre_http = "http://127.0.0.1:8000"

    def test_get_recommendation(self):
        data = {'artist': 'die Ärzte', 'number': 5}
        url = self.pre_http + reverse('artist-recommendation-api')
        response = self.client.post(url, data=data)
        recommendations = json.loads(response.content.decode("utf-8"))['recommendations']
        self.assertEqual(5, len(recommendations))
        self.assertEqual(response.status_code, 200)
