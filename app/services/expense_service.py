from app import db
from app.models import Expense, Participant
from app.utils import calculate_splits
from app.validation import validate_expense_input

class ExpenseService:
    @staticmethod
    def add_expense(data):
        validation_error = validate_expense_input(data)
        if validation_error:
            return {"error": validation_error}, 400

        expense = Expense(
            description=data['description'],
            amount=data['amount'],
            split_method=data['split_method'],
            user_id=data['user_id']
        )
        db.session.add(expense)
        db.session.commit()

        splits = calculate_splits(expense, data['participants'])
        for split in splits:
            participant = Participant(
                user_id=split['user_id'],
                expense_id=expense.id,
                amount=split['amount']
            )
            db.session.add(participant)

        db.session.commit()
        return {"message": "Expense added successfully"}, 201

    @staticmethod
    def get_user_expenses(user_id):
        expenses = Expense.query.filter_by(user_id=user_id).all()
        result = []
        for expense in expenses:
            participants = Participant.query.filter_by(expense_id=expense.id).all()
            participant_data = [
                {"user_id": participant.user_id, "amount": participant.amount}
                for participant in participants
            ]
            result.append({
                "id": expense.id,
                "description": expense.description,
                "amount": expense.amount,
                "split_method": expense.split_method,
                "participants": participant_data
            })
        return result

    @staticmethod
    def get_overall_expenses():
        expenses = Expense.query.all()
        result = []
        for expense in expenses:
            participants = Participant.query.filter_by(expense_id=expense.id).all()
            participant_data = [
                {"user_id": participant.user_id, "amount": participant.amount}
                for participant in participants
            ]
            result.append({
                "id": expense.id,
                "description": expense.description,
                "amount": expense.amount,
                "split_method": expense.split_method,
                "participants": participant_data
            })
        return result
