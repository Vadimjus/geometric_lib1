# Общее описание решения
Geometric Lib - библиотека, написанная на Python, предоставляющая функция для вычисления геометрических характеристик фигур (квадрат, окружность, треугольник). Библиотеку можно использовать в других проектах, импортировав ее и соответствующие функции.

Возможности
- Вычисление периметра и полупериметра треугольника
- Вычисление площади и периметра квадрата
- Вычисление площади и периметра окружности

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание каждой функции с примерами вызова
-  Калькулятор:
    Функция для вычисления площади или периметра данной фигуры:
	Параметры:
		fig (str) - название фигуры
		func (str) - название функции
		size (list) - размер
	Возвращаемое значение:
		Функция ничего не возвращает

-  Функция для вычисления полупериметра треугольника:
    Параметры:
        a,b,c (int) - стороны треугольника
    Возвращаемое значение:
       (a + b + c) / 2 - полупериметр
    '''
    def area(a, b, c):
        return (a + b + c) / 2
    '''

-  Функция для вычисления периметра треугольника:
    Параметры:
        a,b,c (int) - стороны треугольника
    Возвращаемое значение:
       a + b + c - периметр
    '''
    def perimeter(a, b, c):
        return a + b + c 
    '''
    Пример:
    '''
    side_a = 3
    side_b = 4
    side_c = 5

    semi_perimeter = area(side_a, side_b, side_c)
    print(f"Полупериметр треугольника: {semi_perimeter}")

    triangle_perimeter = perimeter(side_a, side_b, side_c)
    print(f"Периметр треугольника: {triangle_perimeter}")
    '''

- Функция для вычисления площади квадрата
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        a*a - площадь квадрата 
    '''
    def area(a):
        return a * a
    '''
    Пример:
    '''
    from geometric_lib import area
        square_area=area(2,2)
        print(square_area)
    '''
    Выходные данные: 4

- Функция для вычисления периметра квадрата
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        4*a - периметр квадрата 
    '''
    def perimeter(a):
        return 4 * a
    '''
    Пример:
    '''
    from geometric_lib import perimeter
        perimeter_area=perimeter(22)
        print(perimeter_area)
    '''
    Выходные данные: 8

- Функция для вычисления площади круга
    Параметры:
        r(int) - радиус круга
    Возращаемое значение:
        pi*r*r - площадь круга 
    '''
    import math
    def area(r):
        return math.pi * r * r
    '''
    Пример:
    '''
    from geometric_lib import area
        circle_area=area(5)
        print(circle_area)
    '''
    Выходные данные: 78.53981633974483
- Функция для вычисления периметра круга
    Параметры:
        r (int) - радиус круга
    Возвращаемое значение:
        2*pi*r - периметр круга
    '''
    def perimeter(r):
        return 2 * math.pi * r
    '''
    Пример:
    '''
    from geometric_lib import perimeter
        circle_perimeter=perimeter(5)
        print(circle_perimeter)
    '''
    Выходные данные: 31.41592653589793
# История изменения проекта с хешами комитов
b5b0fae
d76db2a
51c40eb
d080c78
d078c8d
8ba9aeb