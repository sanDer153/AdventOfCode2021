height_map = []
with open('day_9_input.txt') as f:
    for row in f:
        height_map.append(list(map(int, list(row.strip()))))


def first_star():
    dimension = len(height_map)
    sum_riskfactor = 0

    for row in range(dimension):
        for col in range(dimension):
            if (row == 0 or height_map[row-1][col] > height_map[row][col]) and \
                (col == 0 or height_map[row][col-1] > height_map[row][col]) and \
                (row == dimension - 1 or height_map[row+1][col] > height_map[row][col]) and \
                (col == dimension - 1 or height_map[row][col+1] > height_map[row][col]):

                sum_riskfactor += 1 + height_map[row][col]

    print(sum_riskfactor)


def second_star():
    dimension = len(height_map)
    largest = 0
    second_largest = 0
    third_largest = 0

    for row in range(dimension):
        for col in range(dimension):
            if (row == 0 or height_map[row - 1][col] > height_map[row][col]) and \
                    (col == 0 or height_map[row][col - 1] > height_map[row][col]) and \
                    (row == dimension - 1 or height_map[row + 1][col] > height_map[row][col]) and \
                    (col == dimension - 1 or height_map[row][col + 1] > height_map[row][col]):
                if basin_size(row, col) > largest:
                    third_largest = second_largest
                    second_largest = largest
                    largest = basin_size(row, col)
                elif basin_size(row, col) > second_largest:
                    third_largest = second_largest
                    second_largest = basin_size(row, col)
                elif basin_size(row, col) > third_largest:
                    third_largest = basin_size(row, col)

    print(largest * second_largest *third_largest)


def basin_size(row, col):
    basin = {(row, col)}
    new_to_basin = basin.copy()

    while len(new_to_basin) != 0:
        for (row, col) in basin:
            if row > 0 and height_map[row - 1][col] < 9:
                new_to_basin.update({(row-1, col)})
            if col > 0 and height_map[row][col - 1] < 9:
                new_to_basin.update({(row, col-1)})
            if row < 99 and height_map[row + 1][col] < 9:
                new_to_basin.update({(row+1, col)})
            if col < 99 and height_map[row][col + 1] < 9:
                new_to_basin.update({(row, col+1)})
        new_to_basin = new_to_basin - basin
        basin.update(new_to_basin)


    return len(basin)


first_star()
second_star()