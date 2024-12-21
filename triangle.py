def valid_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)

def area(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("value error, value cannot contain letters")
    if any(x <= 0 for x in (a, b, c)):
        raise ValueError("value error, the value must be greater than 0")
    if not valid_triangle(a, b, c):
        raise ValueError("value error, the property of triangles is not fulfilled")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError("value error, value cannot contain letters")
    if any(x <= 0 for x in (a, b, c)):
        raise ValueError("value error, the value must be greater than 0")
    if not valid_triangle(a, b, c):
        raise ValueError("value error, the property of triangles is not fulfilled")
    return a + b + c