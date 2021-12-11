


def first_star():
    matrix = [[5, 6, 6, 5, 1, 1, 4, 5, 5, 4],
              [4, 8, 8, 2, 6, 6, 5, 4, 2, 7],
              [6, 1, 8, 5, 5, 8, 2, 1, 1, 3],
              [7, 7, 6, 2, 8, 5, 2, 7, 4, 4],
              [7, 2, 5, 5, 6, 2, 1, 8, 4, 1],
              [8, 8, 4, 2, 7, 5, 3, 1, 2, 3],
              [8, 2, 2, 5, 3, 7, 2, 1, 7, 6],
              [7, 2, 1, 2, 8, 6, 5, 8, 2, 7],
              [7, 7, 5, 8, 7, 5, 1, 1, 5, 7],
              [1, 8, 2, 8, 5, 4, 4, 5, 6, 3]]
    flashes = 0
    for step in range(100):
        for row in range(10):
            for col in range(10):
                matrix[row][col] += 1

        found_new_flashes = True
        while found_new_flashes:
            found_new_flashes = False
            for row in range(10):
                for col in range(10):
                    if matrix[row][col] > 9:
                        flash(matrix, row, col)
                        flashes += 1
                        found_new_flashes = True

    print(flashes)

def flash(matrix, row, col):
    if row > 0 and col > 0 and matrix[row-1][col-1] != 0:
        matrix[row-1][col-1] += 1
    if row > 0 and matrix[row-1][col] != 0:
        matrix[row-1][col] += 1
    if row > 0 and col < 9 and matrix[row-1][col+1] != 0:
        matrix[row-1][col+1] += 1
    if col < 9 and matrix[row][col+1] != 0:
        matrix[row][col+1] += 1
    if row < 9 and col < 9 and matrix[row+1][col+1] != 0:
        matrix[row+1][col+1] += 1
    if row < 9 and matrix[row+1][col] != 0:
        matrix[row+1][col] += 1
    if row < 9 and col > 0 and matrix[row+1][col-1] != 0:
        matrix[row+1][col-1] += 1
    if col > 0 and matrix[row][col-1] != 0:
        matrix[row][col-1] += 1

    matrix[row][col] = 0


def second_star():
    matrix = [[5, 6, 6, 5, 1, 1, 4, 5, 5, 4],
              [4, 8, 8, 2, 6, 6, 5, 4, 2, 7],
              [6, 1, 8, 5, 5, 8, 2, 1, 1, 3],
              [7, 7, 6, 2, 8, 5, 2, 7, 4, 4],
              [7, 2, 5, 5, 6, 2, 1, 8, 4, 1],
              [8, 8, 4, 2, 7, 5, 3, 1, 2, 3],
              [8, 2, 2, 5, 3, 7, 2, 1, 7, 6],
              [7, 2, 1, 2, 8, 6, 5, 8, 2, 7],
              [7, 7, 5, 8, 7, 5, 1, 1, 5, 7],
              [1, 8, 2, 8, 5, 4, 4, 5, 6, 3]]
    step = 0
    in_sync = False
    while not in_sync:
        for row in range(10):
            for col in range(10):
                matrix[row][col] += 1

        found_new_flashes = True
        while found_new_flashes:
            found_new_flashes = False
            for row in range(10):
                for col in range(10):
                    if matrix[row][col] > 9:
                        flash(matrix, row, col)
                        found_new_flashes = True

        in_sync = True
        for row in range(10):
            for col in range(10):
                if matrix[row][col] != 0:
                    in_sync = False
        step += 1

    print(step)


first_star()
second_star()