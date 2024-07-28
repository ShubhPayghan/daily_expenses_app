from flask_restful import Resource
from flask import request, send_file
from app import db
from app.models import User, Expense, Participant
from app.validation import validate_expense_input
from app.utils import calculate_splits
from app.balance_sheet import generate_balance_sheet
from app.services.user_service import UserService
from app.services.expense_service import ExpenseService

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        return UserService.create_user(data)

    def get(self, user_id):
        return UserService.get_user_details(user_id)

class ExpenseResource(Resource):
    def post(self):
        data = request.get_json()
        return ExpenseService.add_expense(data)

    def get(self, user_id):
        return ExpenseService.get_user_expenses(user_id)

class OverallExpenseResource(Resource):
    def get(self):
        return ExpenseService.get_overall_expenses()

class BalanceSheetResource(Resource):
    def get(self):
        file_path = generate_balance_sheet()
        return send_file(file_path, as_attachment=True)

def initialize_routes(api):
    api.add_resource(UserResource, '/users', '/users/<int:user_id>')
    api.add_resource(ExpenseResource, '/expenses', '/expenses/<int:user_id>')
    api.add_resource(OverallExpenseResource, '/overall_expenses')
    api.add_resource(BalanceSheetResource, '/balance_sheet')
