def unique_in_order(iterable):
    result = []
    for index in range(len(iterable)):
        if iterable[index] != iterable[index-1]:
            result.append(iterable[index])
    return result