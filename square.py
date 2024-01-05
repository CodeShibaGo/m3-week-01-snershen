import math
def is_square(n):
    result = math.sqrt(n)
    if result == int(result):
        return True
    else:
        return False

