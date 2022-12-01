import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [5, 8, 23, 16, 21, 18, 17]
        self.scores_tie = [21, 21, 22, 20]
        self.scores_two = [16, 15]
        self.scores_one = [10]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest(self):
        result = latest(self.scores)
        self.assertEqual(17, result)
    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        result = personal_best(self.scores)
        self.assertEqual(23, result)

    # # Test top three from list of scores
    def test_personal_top_three(self):
        result = personal_top_three(self.scores)
        self.assertEqual([23, 21, 18], result)

    # # Test ordered from highest tp lowest
    def test_highest_to_lowest(self):
        result = highest_to_lowest(self.scores)
        self.assertEqual([23, 21, 18, 17, 16, 8, 5], result)

    # # Test top three when there is a tie
    def test_top_three_tie(self):
        result = top_three_tie(self.scores_tie)
        self.assertEqual([22, 21, 20], result)

    # # Test top three when there are less than three
    def test_top_three_when_two(self):
        result = top_three_less_than_three(self.scores_two)
        self.assertEqual([16, 15], result)

    # # # Test top three when there is only one
    def test_top_three_less_than_three(self):
        result = top_three_less_than_three(self.scores_one)
        self.assertEqual([10], result)
