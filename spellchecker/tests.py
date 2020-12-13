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
        response = request(method='GET', url=BASE + "spellcheck/car")
        self.assertEqual(response.status_code, 200)
        expected = {"suggestions": [], "correct": True}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_suggestions_one(self):
        response = request(method='GET', url=BASE + "spellcheck/woRka")
        self.assertEqual(response.status_code, 200)
        expected = {
            "suggestions": [
                "workability",
                "workable",
                "workableness",
                "workaday",
                "workaholic",
                "workaholics",
                "workaholism"
            ],
            "correct": False
        }
        self.assertEqual(response.json(), expected)

    def test_spellcheck_single_char(self):
        response = request(method='GET', url=BASE + "spellcheck/a")
        self.assertEqual(response.status_code, 200)
        expected = {"suggestions": [], "correct": True}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_double_char(self):
        response = request(method='GET', url=BASE + "spellcheck/aa")
        self.assertEqual(response.status_code, 404)
        expected = {"message": "Word: aa not found."}
        self.assertEqual(response.json(), expected)

    def test_spellcheck_multiple_duplicate_char(self):
        response = request(method='GET', url=BASE + "spellcheck/aaa")
        self.assertEqual(response.status_code, 404)
        output = 'Word: aaa not found.' in response.text
        expected = True
        self.assertEqual(output, expected)

    def test_spellcheck_suggestions_two(self):
        response = request(method='GET', url=BASE + "spellcheck/aH")
        self.assertEqual(response.status_code, 200)
        expected = {
            "suggestions": [
                "ah",
                "aha",
                "ahchoo",
                "ahead",
                "ahem",
                "ahems",
                "ahimsa",
                "ahimsas",
                "ahold",
                "ahorse",
                "ahoy",
                "ahs"
            ],
            "correct": False
        }
        self.assertEqual(response.json(), expected)

    def test_spellcheck_word_not_found(self):
        response = request(method='GET', url=BASE + "spellcheck/karaoke")
        self.assertEqual(response.status_code, 404)
        output = 'Word: karaoke not found.' in response.text
        expected = True
        self.assertEqual(output, expected)

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

