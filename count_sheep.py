def count_sheep(sheep):
    count = 0
    for el in sheep:
        if el == True:
            count += 1
    return count
