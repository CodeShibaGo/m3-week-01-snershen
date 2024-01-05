def categorize_new_member(data):
    record_list = []
    for age, score in data:
        if age >= 55 and score > 7:
            record_list.append('Senior')
        else:
            record_list.append('Open')
    return record_list