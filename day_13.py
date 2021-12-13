instructions = ['x=655', 'y=447', 'x=327', 'y=223', 'x=163', 'y=111', 'x=81', 'y=55', 'x=40', 'y=27', 'y=13', 'y=6']
input_list = []
matrix = []
with open('day_13_input.txt') as f:
    input_list = [tuple(map(int, x.strip().split(','))) for x in f]

max_x = max([x[0] for x in input_list])
max_y = max([x[1] for x in input_list])

matrix_width = max_x + 1
matrix_height = max_y + 1

def first_star():
    instruction = 'x=655'
    if instruction.split('=')[0] == 'x':
        foldline = int(instruction.split('=')[1])
        new_matrix_width = max(foldline, matrix_width - (foldline + 1))
        new_matrix_height = matrix_height

        for index in range(len(input_list)):
            input_list[index] = (new_matrix_width - abs(foldline - input_list[index][0]),input_list[index][1])
    else:
        foldline = int(instruction.split('=')[1])
        new_matrix_width = matrix_width
        new_matrix_height = max(foldline, matrix_height - (foldline + 1))

        for index in range(len(input_list)):
            input_list[index] = (input_list[index][0], new_matrix_height - abs(foldline - input_list[index][1]))

    print(len(list(set(input_list))))


def second_star():
    matrix_width = max_x + 1
    matrix_height = max_y + 1
    points = input_list
    for instruction in instructions:
        if instruction.split('=')[0] == 'x':
            foldline = int(instruction.split('=')[1])
            new_matrix_width = max(foldline, matrix_width - (foldline + 1))
            new_matrix_height = matrix_height

            for index in range(len(points)):
                points[index] = (new_matrix_width - abs(foldline - points[index][0]), points[index][1])

            matrix_width = new_matrix_width
            matrix_height = new_matrix_height
        else:
            foldline = int(instruction.split('=')[1])
            new_matrix_width = matrix_width
            new_matrix_height = max(foldline, matrix_height - (foldline + 1))

            for index in range(len(points)):
                points[index] = (points[index][0], new_matrix_height - abs(foldline - points[index][1]))

            matrix_width = new_matrix_width
            matrix_height = new_matrix_height

        points = list(set(points))

    for row in range(matrix_height):
        matrix.append(['.' for x in range(matrix_width)])

    for (x, y) in points:
        matrix[y][x] = '@'

    for line in matrix:
        print("".join(line))


first_star()
second_star()
