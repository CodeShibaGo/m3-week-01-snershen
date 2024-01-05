def disemvowel(s):
    vowels = 'aeiou'
    result = ''
    for letter in s:
        if letter.lower() not in vowels:
            result += letter
    return result
