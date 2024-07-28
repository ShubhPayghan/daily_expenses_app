from app import db
from app.models import User

class UserService:
    @staticmethod
    def create_user(data):
        user = User(email=data['email'], name=data['name'], mobile=data['mobile'])
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}, 201

    @staticmethod
    def get_user_details(user_id):
        user = User.query.get_or_404(user_id)
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "mobile": user.mobile
        }
