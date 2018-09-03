from django.test import TestCase
from recommender_app.ml_model.recommender import get_artist_recommendations


class RecommenderTest(TestCase):

    def test_artist_recommendation(self):
        artist = "die Ärzte"
        result_len = 5
        result = get_artist_recommendations(artist, 5)
        self.assertEqual(len(result), result_len)
