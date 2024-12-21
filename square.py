
def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if a < 0:
        raise ValueError("value error, the value must be greater than 0")
    return a * a

    '''
    Функция для вычисления площади квадрата:
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        a*a - площадь квадрата 
    '''

def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if a < 0:
        raise ValueError("value error, the value must be greater than 0")
    return 4 * a

    '''
    Функция для вычисления периметра квадрата:
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        4*a - периметр квадрата 
    '''
    