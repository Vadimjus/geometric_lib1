import math


def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if r < 0:
        raise ValueError("value error, the value must be greater than 0")
    return math.pi * r * r
    
    '''
    Функция для вычисления площади круга:
    Параметры:
        r(int) - радиус круга
    Возращаемое значение:
        pi*r*r - площадь круга
    ''' 

def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError("value error, value cannot contain letters")
    if r < 0:
        raise ValueError("value error, the value must be greater than 0")
    return 2 * math.pi * r

    '''
    Функция для вычисления периметра круга:
    Параметры:
        r (int) - радиус круга
    Возвращаемое значение:
        2*pi*r - периметр круга
    '''