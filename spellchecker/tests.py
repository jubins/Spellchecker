from requests import request
import unittest

BASE = "http://localhost:31337/"


class TestSpellchecker(unittest.TestCase):

    def test_homepage(self):
        response = request(method='GET', url=BASE)
        self.assertEqual(response.status_code, 200)
        expected = {"message": "Welcome to the Spellchecker API! Go to http://localhost:31337/spellchecker/{word} to spellcheck."}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_correct_word(self):
        response = request(method='GET', url=BASE + "http://localhost:31337/spellcheck/car")
        self.assertEqual(response.status_code, 200)
        expected = {"suggestions": [], "correct": True}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_suggestions(self):
        response = request(method='GET', url=BASE + "http://localhost:31337/spellcheck/caR")
        self.assertEqual(response.status_code, 200)
        expected = {"suggestions": [], "correct": True}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_word_not_found(self):
        response = request(method='GET', url=BASE + "http://localhost:31337/spellcheck/karaoke")
        self.assertEqual(response.status_code, 404)
        expected = {'message': f'Word: karaoke not found.'}
        self.assertEqual(response.json(), expected)

    def test_invalid_url_one(self):
        response = request(method='GET', url=BASE + "spellchecker/")
        self.assertEqual(response.status_code, 404)

    def test_invalid_url_two(self):
        response = request(method='GET', url=BASE + "spellch/")
        self.assertEqual(response.status_code, 404)

    def test_query_params_not_allowed(self):
        response = request(method='GET', url=BASE + "spellcheck/word?word=car")
        self.assertEqual(response.status_code, 400)
        expected = {"message": "Unknown arguments: word"}
        self.assertEqual(response.json(), expected)


if __name__ == '__main__':
    unittest.main()

