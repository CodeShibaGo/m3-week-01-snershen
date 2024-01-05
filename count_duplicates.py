def count_duplicates(text):
    text_list = {}
    for el in text.lower():
        if el in text_list:
            text_list[el] += 1
        else:
            text_list[el] = 1
    count = 0
    for el in text_list:
        if text_list[el] > 1:
            count += 1
    return count