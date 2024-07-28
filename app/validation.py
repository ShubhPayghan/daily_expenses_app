def validate_expense_input(data):
    if 'split_method' not in data or data['split_method'] not in ['equal', 'exact', 'percentage']:
        return "Invalid split method"
    if data['split_method'] == 'percentage':
        total_percentage = sum(p['percentage'] for p in data['participants'])
        if total_percentage != 100:
            return "Total percentage must add up to 100"
    return None
