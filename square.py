def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if a < 0:
        raise ValueError("value error, the value must be greater than 0")
    return a * a


def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if a < 0:
        raise ValueError("value error, the value must be greater than 0")
    return 4 * a
