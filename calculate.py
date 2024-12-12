import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'area-circle': 1,
    'perimeter-circle': 1,
    'area-square': 1,
    'perimeter-square': 1
}

def calc(fig, func, size):
    assert fig in figs, f"Invalid figure. Choose from: {figs}"
    assert func in funcs, f"Invalid operation. Choose from: {funcs}"

    if not isinstance(size, list):
        raise TypeError("The size parameter must be a list.")
    if not size:
        raise TypeError("The size list cannot be empty.")
    if not all(isinstance(x, (int, float)) for x in size):
        raise TypeError("All elements in the size list must be numeric.")

    if fig == 'circle':
        if len(size) != 1:
            raise TypeError("A circle requires exactly one parameter.")
        if func == 'area':
            return circle.area(size[0])
        return circle.perimeter(size[0])

    if fig == 'square':
        if len(size) != 1:
            raise TypeError("A square requires exactly one parameter.")
        if func == 'area':
            return square.area(size[0])
        return square.perimeter(size[0])

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter the type of figure (options: {figs}):\n")

    while func not in funcs:
        func = input(f"Choose an operation to perform (options: {funcs}):\n")

    params = 1
    while len(size) != params:
        try:
            size = list(map(float, input(f"Provide {params} dimension(s) for the figure, separated by spaces:\n").split()))
        except ValueError:
            print("Input must be valid numbers. Please try again.")
            continue

    try:
        result = calc(fig, func, size)
        print(f'The {func} of the {fig} is {result}')
    except (ValueError, TypeError, AssertionError) as e:
        print(f"An error occurred: {e}")
