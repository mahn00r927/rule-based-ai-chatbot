import unittest
from chatbot_utils import get_response


class TestDecodeBot(unittest.TestCase):

    def test_greeting(self):
        response, response_type = get_response("hello")
        self.assertEqual(response_type, "greeting")

    def test_name(self):
        response, response_type = get_response("what is your name")
        self.assertIn("DecodeBot", response)

    def test_ai(self):
        response, response_type = get_response("what is ai")
        self.assertIn("Artificial Intelligence", response)

    def test_python(self):
        response, response_type = get_response("what is python")
        self.assertIn("Python", response)

    def test_calculator(self):
        response, response_type = get_response("10+5")
        self.assertEqual(response, "Result: 15")
        self.assertEqual(response_type, "calculation")

    def test_square(self):
        response, response_type = get_response("square of 5")
        self.assertEqual(response, "Result: 25")
        self.assertEqual(response_type, "calculation")

    def test_cube(self):
        response, response_type = get_response("cube of 3")
        self.assertEqual(response, "Result: 27")
        self.assertEqual(response_type, "calculation")

    def test_sqrt(self):
        response, response_type = get_response("sqrt 81")
        self.assertEqual(response, "Result: 9")
        self.assertEqual(response_type, "calculation")

    def test_unknown(self):
        response, response_type = get_response("abcdefgh")
        self.assertEqual(response_type, "general")


if __name__ == "__main__":
    unittest.main()