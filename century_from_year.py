def century(year):
    result = year // 100
    if year % 100 == 0:
        return result
    else:
        return result+1