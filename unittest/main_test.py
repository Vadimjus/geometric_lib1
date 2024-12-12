import pytest
import math
import circle
import square
import triangle
import calculate

def test_area_circle_positive_radius():
    radii = [1, 2, 1.5]
    expected_areas = [math.pi, math.pi * 4, round(7.07, 2)]
    
    for radius, expected in zip(radii, expected_areas):
        assert round(circle.area(radius), 2) == expected

def test_area_circle_zero_radius():
    assert circle.area(0) == 0

@pytest.mark.parametrize("radius,expected", [
    (1, math.pi),
    (2, math.pi * 4),
    (0.5, math.pi * 0.25),
    (10, math.pi * 100)
])
def test_area_circle_various_radii(radius, expected):
    assert circle.area(radius) == expected

@pytest.mark.parametrize("radius", [-1, -2.5, -100])
def test_area_circle_negative_radius(radius):
    with pytest.raises(ValueError):
        circle.area(radius)

@pytest.mark.parametrize("invalid_input", ["2", [1], None])
def test_area_circle_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        circle.area(invalid_input)

def test_perimeter_circle_positive_radius():
    radii = [1, 2, 1.5]
    expected_perimeters = [2 * math.pi, 4 * math.pi, round(9.42, 2)]
    
    for radius, expected in zip(radii, expected_perimeters):
        assert round(circle.perimeter(radius), 2) == expected

def test_perimeter_circle_zero_radius():
    assert circle.perimeter(0) == 0

@pytest.mark.parametrize("radius,expected", [
    (1, 2 * math.pi),
    (2, 4 * math.pi),
    (0.5, math.pi),
    (10, 20 * math.pi)
])
def test_perimeter_circle_various_radii(radius, expected):
    assert circle.perimeter(radius) == expected

@pytest.mark.parametrize("radius", [-1, -2.5, -100])
def test_perimeter_circle_negative_radius(radius):
    with pytest.raises(ValueError):
        circle.perimeter(radius)

@pytest.mark.parametrize("invalid_input", ["2", [1], None])
def test_perimeter_circle_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        circle.perimeter(invalid_input)

def test_area_square_positive_side():
    sides = [1, 2, 1.5]
    expected_areas = [1, 4, 2.25]
    
    for side, expected in zip(sides, expected_areas):
        assert square.area(side) == expected

def test_area_square_zero_side():
    assert square.area(0) == 0

@pytest.mark.parametrize("side,expected", [
    (1, 1),
    (2, 4),
    (0.5, 0.25),
    (10, 100)
])
def test_area_square_various_sides(side, expected):
    assert square.area(side) == expected

@pytest.mark.parametrize("side", [-1, -2.5, -100])
def test_area_square_negative_side(side):
    with pytest.raises(ValueError):
        square.area(side)

@pytest.mark.parametrize("invalid_input", ["2", [1], None])
def test_area_square_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        square.area(invalid_input)

def test_perimeter_square_positive_side():
    sides = [1, 2, 1.5]
    expected_perimeters = [4, 8, 6]
    
    for side, expected in zip(sides, expected_perimeters):
        assert square.perimeter(side) == expected

def test_perimeter_square_zero_side():
    assert square.perimeter(0) == 0

@pytest.mark.parametrize("side,expected", [
    (1, 4),
    (2, 8),
    (0.5, 2),
    (10, 40)
])
def test_perimeter_square_various_sides(side, expected):
    assert square.perimeter(side) == expected

@pytest.mark.parametrize("side", [-1, -2.5, -100])
def test_perimeter_square_negative_side(side):
    with pytest.raises(ValueError):
        square.perimeter(side)

@pytest.mark.parametrize("invalid_input", ["2", [1], None])
def test_perimeter_square_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        square.perimeter(invalid_input)

def test_area_triangle_positive_sides():
    triangles = [(3, 4, 5), (5, 12, 13), (2, 3, 4)]
    expected_areas = [6, 30, round(2.90, 2)]
    
    for sides, expected in zip(triangles, expected_areas):
        assert round(triangle.area(*sides), 2) == expected

@pytest.mark.parametrize("sides", [(0, 1, 1), (1, 0, 1), (1, 1, 0)])
def test_area_triangle_zero_sides(sides):
    with pytest.raises(ValueError):
        triangle.area(*sides)

@pytest.mark.parametrize("sides,expected", [
    ((3, 4, 5), 6),
    ((5, 12, 13), 30),
    ((6, 8, 10), 24),
    ((9, 12, 15), 54)
])
def test_area_triangle_various_sides(sides, expected):
    assert triangle.area(*sides) == expected

@pytest.mark.parametrize("sides", [
    (-1, 2, 2),
    (2, -1, 2),
    (2, 2, -1),
    (-1, -1, -1)
])
def test_area_triangle_negative_sides(sides):
    with pytest.raises(ValueError):
        triangle.area(*sides)

@pytest.mark.parametrize("sides", [(1, 1, 3), (1, 3, 1), (3, 1, 1)])
def test_area_triangle_invalid_triangle(sides):
    with pytest.raises(ValueError):
        triangle.area(*sides)

@pytest.mark.parametrize("sides", [("2", 2, 2), (2, [2], 2), (2, 2, None)])
def test_area_triangle_invalid_types(sides):
    with pytest.raises(TypeError):
        triangle.area(*sides)

def test_perimeter_triangle_positive_sides():
    triangles = [(3, 4, 5), (5, 12, 13), (2, 3, 4)]
    expected_perimeters = [12, 30, 9]
    
    for sides, expected in zip(triangles, expected_perimeters):
        assert triangle.perimeter(*sides) == expected

@pytest.mark.parametrize("sides", [(0, 1, 1), (1, 0, 1), (1, 1, 0)])
def test_perimeter_triangle_zero_sides(sides):
    with pytest.raises(ValueError):
        triangle.perimeter(*sides)

@pytest.mark.parametrize("sides,expected", [
    ((3, 4, 5), 12),
    ((5, 12, 13), 30),
    ((6, 8, 10), 24),
    ((9, 12, 15), 36)
])
def test_perimeter_triangle_various_sides(sides, expected):
    assert triangle.perimeter(*sides) == expected

@pytest.mark.parametrize("sides", [
    (-1, 2, 2),
    (2, -1, 2),
    (2, 2, -1),
    (-1, -1, -1)
])
def test_perimeter_triangle_negative_sides(sides):
    with pytest.raises(ValueError):
        triangle.perimeter(*sides)

@pytest.mark.parametrize("sides", [(1, 1, 3), (1, 3, 1), (3, 1, 1)])
def test_perimeter_triangle_invalid_triangle(sides):
    with pytest.raises(ValueError):
        triangle.perimeter(*sides)

@pytest.mark.parametrize("sides", [("2", 2, 2), (2, [2], 2), (2, 2, None)])
def test_perimeter_triangle_invalid_types(sides):
    with pytest.raises(TypeError):
        triangle.perimeter(*sides)


def test_circle_calculations():
    figure = 'circle'
    operation = 'area'
    size = [2]
    expected = math.pi * 4

    result = calculate.calc(figure, operation, size)
    assert result == expected

def test_square_calculations():
    figure = 'square'
    operation = 'area'
    size = [2]
    expected = 4

    result = calculate.calc(figure, operation, size)
    assert result == expected

def test_invalid_figure_calculation():
    figure = 'triangle'
    operation = 'area'
    size = [1]

    with pytest.raises(AssertionError):
        calculate.calc(figure, operation, size)

def test_invalid_operation_calculation():
    figure = 'circle'
    operation = 'volume'
    size = [1]

    with pytest.raises(AssertionError):
        calculate.calc(figure, operation, size)

def test_negative_size_calculations():
    test_cases = [
        {'figure': 'circle', 'operation': 'area', 'size': [-1]},
        {'figure': 'circle', 'operation': 'perimeter', 'size': [-2]},
        {'figure': 'square', 'operation': 'area', 'size': [-3]},
        {'figure': 'square', 'operation': 'perimeter', 'size': [-4]}
    ]
    for test_input in test_cases:
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        with pytest.raises(ValueError):
            calculate.calc(figure, operation, size)

def test_invalid_input_types_calculation():
    test_cases = [
        {'figure': 'circle', 'operation': 'area', 'size': ["string"]},
        {'figure': 'square', 'operation': 'perimeter', 'size': [None]}
    ]
    for test_input in test_cases:
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        with pytest.raises(TypeError):
            calculate.calc(figure, operation, size)

def test_empty_size_list_calculation():
    figure = 'circle'
    operation = 'area'
    size = []

    with pytest.raises(TypeError):
        calculate.calc(figure, operation, size)

def test_main_integration_calculation(monkeypatch):
    inputs = ['circle', 'area', '2']
    expected = math.pi * 4
    input_mock = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_mock))

    if hasattr(calculate, 'main'):
        result = calculate.main()
    else:
        result = calculate.calc('circle', 'area', [2])

    assert result == expected

def test_sizes_dict_calculation():
    assert isinstance(calculate.sizes, dict)
    assert isinstance(calculate.figs, list)
    assert isinstance(calculate.funcs, list)

def test_available_figures_calculation():
    expected_figures = ['circle', 'square']
    for figure in expected_figures:
        assert figure in calculate.figs

def test_available_functions_calculation():
    expected_functions = ['area', 'perimeter']
    for function in expected_functions:
        assert function in calculate.funcs

def test_calculations_valid():
    test_cases = [
        (
            {'figure': 'circle', 'operation': 'area', 'size': [1]},
            math.pi
        ),
        (
            {'figure': 'circle', 'operation': 'perimeter', 'size': [1]},
            2 * math.pi
        ),
        (
            {'figure': 'square', 'operation': 'area', 'size': [1]},
            1
        ),
        (
            {'figure': 'square', 'operation': 'perimeter', 'size': [1]},
            4
        )
    ]
    for test_input, expected in test_cases:
        figure = test_input['figure']
        operation = test_input['operation']
        size = test_input['size']

        result = calculate.calc(figure, operation, size)
        assert result == expected