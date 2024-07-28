import unittest
from app import create_app, db
from app.models import User, Expense, Participant
from app.services.user_service import UserService
from app.services.expense_service import ExpenseService

class TestServices(unittest.TestCase):
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

    def test_create_user(self):
        user_data = {
            'email': 'test@example.com',
            'name': 'Test User',
            'mobile': '1234567890'
        }
        user = UserService.create_user(user_data)
        self.assertEqual(user.email, 'test@example.com')

    def test_add_expense(self):
        user = User(email='test@example.com', name='Test User', mobile='1234567890')
        db.session.add(user)
        db.session.commit()

        expense_data = {
            'description': 'Dinner',
            'amount': 100.0,
            'split_method': 'equal',
            'user_id': user.id,
            'participants': [{'user_id': user.id}]
        }
        expense = ExpenseService.add_expense(expense_data)
        self.assertEqual(expense.description, 'Dinner')

if __name__ == '__main__':
    unittest.main()
