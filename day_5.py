# input_list = [((0,9), (5,9)), ((8,0), (0,8)), ((9,4), (3,4)), ((2,2), (2,1)), ((7,0), (7,4)), ((6,4), (2,0)), ((0,9), (2,9)), ((3,4), (1,4)), ((0,0), (8,8)), ((5,5), (8,2))]
with open('day_5_input.txt') as f:
    input_list = [tuple(vent_line.strip().split(' -> ')) for vent_line in f]
    for i in range(len(input_list)):
        (x, y) = input_list[i]
        input_list[i] = (tuple(x.split(',')), tuple(y.split(',')))
        (x, y) = input_list[i]
        (x1, x2) = x
        (y1, y2) = y
        x = (int(x1), int(x2))
        y = (int(y1), int(y2))
        input_list[i] = (x, y)


def first_star():
    dimension = 1000
    # dimension = 10
    matrix = []
    for row in range(dimension):
        matrix.append([0 for x in range(dimension)])

    for vent_line in input_list:
        (begin, end) = vent_line
        (x_begin, y_begin) = begin
        (x_end, y_end) = end
        if x_begin == x_end or y_begin == y_end:
            Dx = x_end - x_begin
            Dy = y_end - y_begin
            if Dx != 0: dx = Dx // abs(Dx)
            else: dx = Dx
            if Dy != 0: dy = Dy // abs(Dy)
            else: dy = Dy

            matrix[y_begin][x_begin] += 1
            while x_begin != x_end:
                x_begin += dx
                matrix[y_begin][x_begin] += 1

            while y_begin != y_end:
                y_begin += dy
                matrix[y_begin][x_begin] += 1

    crossings = 0
    for row in matrix:
        for col in row:
            if col > 1:
                crossings += 1

    print(crossings)


def second_star():
    dimension = 1000
    # dimension = 10
    matrix = []
    for row in range(dimension):
        matrix.append([0 for x in range(dimension)])

    for vent_line in input_list:
        (begin, end) = vent_line
        (x_begin, y_begin) = begin
        (x_end, y_end) = end

        Dx = x_end - x_begin
        Dy = y_end - y_begin
        if Dx != 0: dx = Dx // abs(Dx)
        else: dx = Dx
        if Dy != 0: dy = Dy // abs(Dy)
        else: dy = Dy

        matrix[y_begin][x_begin] += 1
        while x_begin != x_end:
            x_begin += dx
            y_begin += dy
            matrix[y_begin][x_begin] += 1

        while y_begin != y_end:
            x_begin += dx
            y_begin += dy
            matrix[y_begin][x_begin] += 1

    crossings = 0
    for row in matrix:
        for col in row:
            if col > 1:
                crossings += 1

    print(crossings)


first_star()
second_star()
