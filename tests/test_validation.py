import unittest
from app.validation import validate_expense_input

class TestValidation(unittest.TestCase):
    def test_validate_split_method(self):
        data = {'split_method': 'invalid'}
        error = validate_expense_input(data)
        self.assertEqual(error, 'Invalid split method')

    def test_validate_percentage_split(self):
        data = {
            'split_method': 'percentage',
            'participants': [{'percentage': 30}, {'percentage': 50}]
        }
        error = validate_expense_input(data)
        self.assertEqual(error, 'Total percentage must add up to 100')

if __name__ == '__main__':
    unittest.main()
