import unittest
from src.word_reverser import *

class TestWordReverse(unittest.TestCase):
    def setUp(self):
        self.string = "Hey fellow warriors"
        self.string2 = "This is a test"
        self.string3 = "This is another test"

    def test_spinWords(self):
        result = spinWords(self.string)
        self.assertEqual("Hey wollef sroirraw", result)

    def test_spinWords_all_under_five(self):
        result = spinWords(self.string2)
        self.assertEqual("This is a test", result)

    def test_spinWords(self):
        result = spinWords(self.string3)
        self.assertEqual("This is rehtona test", result)

    # Have unit tests for the following sentences 

    # "Hello this is a test fantastic"
    # "The cat was cute and he was called Azzazel"
    # "Very cool hat"
