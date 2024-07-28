import unittest
from app import db, create_app
from app.models import User, Expense, Participant

class TestModels(unittest.TestCase):
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
        user = User(email='test@example.com', name='Test User', mobile='1234567890')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(user.email, 'test@example.com')

    def test_create_expense(self):
        user = User(email='test@example.com', name='Test User', mobile='1234567890')
        db.session.add(user)
        db.session.commit()

        expense = Expense(description='Dinner', amount=100.0, split_method='equal', user_id=user.id)
        db.session.add(expense)
        db.session.commit()
        self.assertEqual(expense.description, 'Dinner')

if __name__ == '__main__':
    unittest.main()
