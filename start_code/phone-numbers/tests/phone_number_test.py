import unittest
from src.phone_number import * 

class TestPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.number = 1234567890

    def test_check_if_input_is_number(self):
        self.assertEqual(int, type(self.number))

    def test_check_number_length(self):
        self.assertEqual(10, len(str(self.number)))

    def test_number_converted_to_string(self):
        result = create_phone_number(self.number)
        self.assertEqual(str, type(result))

    def test_check_for_space(self):
        result = create_phone_number(self.number)
        self.assertEqual(" ", result[5])

    def test_check_for_open_bracket(self):
        result = create_phone_number(self.number)
        self.assertEqual("(", result[0])

    def test_check_for_closed_bracket(self):
        result = create_phone_number(self.number)
        self.assertEqual(")", result[4])

    def test_check_for_dash(self):
        result = create_phone_number(self.number)
        self.assertEqual("-", result[9])
