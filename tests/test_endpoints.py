import unittest
import json
from app import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_detect_language_endpoint(self):
        sample_data = {'text': 'Hello, how are you?'}
        response = self.client.post('/detect_language', data=json.dumps(sample_data), content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('language', data)
        self.assertEqual(data['language'], 'en')

    def test_named_entities_endpoint(self):
        sample_data = {'text': 'Barack Obama was born in Hawaii.'}
        response = self.client.post('/named_entities', data=json.dumps(sample_data), content_type='application/json')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('entities', data)
        self.assertEqual(data['entities'], ['Barack Obama (1)', 'Hawaii (1)'])


if __name__ == '__main__':
    unittest.main()
