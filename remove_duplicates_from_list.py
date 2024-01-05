def distinct(seq):
    result = []
    for el in seq:
        if el not in result:
            result.append(el)
    return result

    """
    python3.6 之後
    return list(dict.fromkeys(seq))
    """