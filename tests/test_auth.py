import unittest
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

class TestAuth(unittest.TestCase):
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

    def test_register_user(self):
        response = self.client.post('/register', json={
            'email': 'test@example.com',
            'name': 'Test User',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        password_hash = generate_password_hash('password123', method='sha256')
        user = User(email='test@example.com', name='Test User', password=password_hash)
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
