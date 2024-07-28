import unittest
from app.utils import calculate_splits

class TestUtils(unittest.TestCase):
    def test_calculate_equal_splits(self):
        expense = {'amount': 100.0, 'split_method': 'equal'}
        participants = [{'user_id': 1}, {'user_id': 2}]
        splits = calculate_splits(expense, participants)
        self.assertEqual(splits[0]['amount'], 50.0)
        self.assertEqual(splits[1]['amount'], 50.0)

    def test_calculate_exact_splits(self):
        expense = {'amount': 100.0, 'split_method': 'exact'}
        participants = [{'user_id': 1, 'amount': 30.0}, {'user_id': 2, 'amount': 70.0}]
        splits = calculate_splits(expense, participants)
        self.assertEqual(splits[0]['amount'], 30.0)
        self.assertEqual(splits[1]['amount'], 70.0)

    def test_calculate_percentage_splits(self):
        expense = {'amount': 100.0, 'split_method': 'percentage'}
        participants = [{'user_id': 1, 'percentage': 30}, {'user_id': 2, 'percentage': 70}]
        splits = calculate_splits(expense, participants)
        self.assertEqual(splits[0]['amount'], 30.0)
        self.assertEqual(splits[1]['amount'], 70.0)

if __name__ == '__main__':
    unittest.main()
