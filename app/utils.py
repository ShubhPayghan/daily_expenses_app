def calculate_splits(expense, participants):
    splits = []
    if expense.split_method == 'equal':
        share = expense.amount / len(participants)
        for participant in participants:
            splits.append({'user_id': participant['user_id'], 'amount': share})
    elif expense.split_method == 'exact':
        for participant in participants:
            splits.append({'user_id': participant['user_id'], 'amount': participant['amount']})
    elif expense.split_method == 'percentage':
        for participant in participants:
            amount = (expense.amount * participant['percentage']) / 100
            splits.append({'user_id': participant['user_id'], 'amount': amount})
    return splits
