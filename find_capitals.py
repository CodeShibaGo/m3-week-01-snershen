def find_capitals(word):
    word_list = word.split(' ')
    record_list = []
    if word == '':
        return ''
    else:
        for index, word in enumerate(word_list):
            if word[0] == word[0].upper():
                record_list.append(word[0])
        return ''.join(record_list)

