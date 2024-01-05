def array_diff(a, b):
    result = []
    for el in a:
        if el not in b:
            result.append(el)
    return result