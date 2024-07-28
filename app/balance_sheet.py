import os
import pandas as pd
from app.models import User, Expense, Participant
from app import db

def generate_balance_sheet():
    expenses = Expense.query.all()
    data = []
    for expense in expenses:
        participants = Participant.query.filter_by(expense_id=expense.id).all()
        for participant in participants:
            user = User.query.get(participant.user_id)
            data.append({
                'description': expense.description,
                'amount': participant.amount,
                'user': user.name
            })

    df = pd.DataFrame(data)
    file_path = 'balance_sheet.xlsx'
    df.to_excel(file_path, index=False)
    return file_path
