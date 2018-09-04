from django.test import TestCase
from recommender_app.ml_model.recommender import get_artist_recommendations


class RecommenderTest(TestCase):

    def test_artist_recommendation(self):
        artist = "die Ärzte"
        result_len = 5
        result = get_artist_recommendations(artist, 5)
        self.assertEqual(len(result), result_len)

    def test_not_available_artist(self):
        artist = "not available"
        result_len = 0
        result = get_artist_recommendations(artist, 5)
        self.assertEqual(len(result), result_len)
