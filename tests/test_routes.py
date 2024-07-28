import unittest
from app import create_app, db

class TestRoutes(unittest.TestCase):
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
        response = self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'mobile': '1234567890'
        })
        self.assertEqual(response.status_code, 201)

    def test_add_expense(self):
        self.client.post('/users', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'mobile': '1234567890'
        })
        response = self.client.post('/expenses', json={
            'description': 'Dinner',
            'amount': 100.0,
            'split_method': 'equal',
            'user_id': 1,
            'participants': [{'user_id': 1}]
        })
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
