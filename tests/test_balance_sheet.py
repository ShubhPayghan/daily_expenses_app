import unittest
from app import create_app, db
from app.models import User, Expense, Participant
from app.balance_sheet import generate_balance_sheet

class TestBalanceSheet(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_generate_balance_sheet(self):
        user = User(email='test@example.com', name='Test User', mobile='1234567890')
        db.session.add(user)
        db.session.commit()

        expense = Expense(description='Dinner', amount=100.0, split_method='equal', user_id=user.id)
        db.session.add(expense)
        db.session.commit()

        participant = Participant(user_id=user.id, expense_id=expense.id, amount=100.0)
        db.session.add(participant)
        db.session.commit()

        file_path = generate_balance_sheet()
        self.assertTrue(file_path.endswith('balance_sheet.xlsx'))

if __name__ == '__main__':
    unittest.main()
