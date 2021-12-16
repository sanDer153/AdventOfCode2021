cave_map = []
with open('day_15_input.txt') as f:
    for line in f:
        cave_map.append(list(map(int, list(line.strip()))))


def first_star():
    unvisited = {(x, y) for x in range(100) for y in range(100)}
    dist = {(0, 0): 0}
    reached_end = False

    while not reached_end:
        min_distance = min([dist[d] for d in unvisited if d in dist])
        (current_row, current_col) = list(filter(lambda x: dist[x] == min_distance and x in unvisited, dist))[0]

        if 0 < current_row:
            if (current_row - 1, current_col) in dist:
                if cave_map[current_row - 1][current_col] + dist[(current_row, current_col)] < dist[(current_row - 1, current_col)]:
                    dist[(current_row - 1, current_col)] = cave_map[current_row - 1][current_col] + dist[(current_row, current_col)]
            else:
                dist[(current_row - 1, current_col)] = cave_map[current_row - 1][current_col] + dist[(current_row, current_col)]

        if 0 < current_col:
            if (current_row, current_col - 1) in dist:
                if cave_map[current_row][current_col - 1] + dist[(current_row, current_col)] < dist[(current_row, current_col - 1)]:
                    dist[(current_row, current_col - 1)] = cave_map[current_row][current_col - 1] + dist[(current_row, current_col)]
            else:
                dist[(current_row, current_col - 1)] = cave_map[current_row][current_col - 1] + dist[(current_row, current_col)]

        if current_row < 99:
            if (current_row + 1, current_col) in dist:
                if cave_map[current_row + 1][current_col] + dist[(current_row, current_col)] < dist[(current_row + 1, current_col)]:
                    dist[(current_row + 1, current_col)] = cave_map[current_row + 1][current_col] + dist[(current_row, current_col)]
            else:
                dist[(current_row + 1, current_col)] = cave_map[current_row + 1][current_col] + dist[(current_row, current_col)]

        if current_col < 99:
            if (current_row, current_col + 1) in dist:
                if cave_map[current_row][current_col + 1] + dist[(current_row, current_col)] < dist[(current_row, current_col + 1)]:
                    dist[(current_row, current_col + 1)] = cave_map[current_row][current_col + 1] + dist[(current_row, current_col)]
            else:
                dist[(current_row, current_col + 1)] = cave_map[current_row][current_col + 1] + dist[(current_row, current_col)]

        if(current_row, current_col) == (99, 99):
            reached_end = True

        unvisited.discard((current_row, current_col))

    print(dist[(99, 99)])


def second_star():
    unvisited = {(x, y) for x in range(500) for y in range(500)}
    dist = {(0, 0): 0}
    reached_end = False

    cave_map_2 = []
    for i in range(500):
        row = [cave_map[i % 100][j % 100] + i // 100 + j // 100 for j in range(500)]
        for x in range(500):
            if row[x] > 9:
                row[x] = row[x] % 9
        cave_map_2.append(row)

    print('map generated')

    while not reached_end:
        min_distance = min([dist[d] for d in unvisited if d in dist])
        (current_row, current_col) = list(filter(lambda x: dist[x] == min_distance and x in unvisited, dist))[0]

        if 0 < current_row:
            if (current_row - 1, current_col) in dist:
                if cave_map_2[current_row - 1][current_col] + dist[(current_row, current_col)] < dist[(current_row - 1, current_col)]:
                    dist[(current_row - 1, current_col)] = cave_map_2[current_row - 1][current_col] + dist[(current_row, current_col)]
            else:
                dist[(current_row - 1, current_col)] = cave_map_2[current_row - 1][current_col] + dist[(current_row, current_col)]

        if 0 < current_col:
            if (current_row, current_col - 1) in dist:
                if cave_map_2[current_row][current_col - 1] + dist[(current_row, current_col)] < dist[(current_row, current_col - 1)]:
                    dist[(current_row, current_col - 1)] = cave_map_2[current_row][current_col - 1] + dist[(current_row, current_col)]
            else:
                dist[(current_row, current_col - 1)] = cave_map_2[current_row][current_col - 1] + dist[(current_row, current_col)]

        if current_row < 499:
            if (current_row + 1, current_col) in dist:
                if cave_map_2[current_row + 1][current_col] + dist[(current_row, current_col)] < dist[(current_row + 1, current_col)]:
                    dist[(current_row + 1, current_col)] = cave_map_2[current_row + 1][current_col] + dist[(current_row, current_col)]
            else:
                dist[(current_row + 1, current_col)] = cave_map_2[current_row + 1][current_col] + dist[(current_row, current_col)]

        if current_col < 499:
            if (current_row, current_col + 1) in dist:
                if cave_map_2[current_row][current_col + 1] + dist[(current_row, current_col)] < dist[(current_row, current_col + 1)]:
                    dist[(current_row, current_col + 1)] = cave_map_2[current_row][current_col + 1] + dist[(current_row, current_col)]
            else:
                dist[(current_row, current_col + 1)] = cave_map_2[current_row][current_col + 1] + dist[(current_row, current_col)]

        if (current_row + current_col) % 100 == 0:
            print((current_row, current_col))

        if(current_row, current_col) == (499, 499):
            reached_end = True

        unvisited.discard((current_row, current_col))

    print(dist[(499, 499)])


# first_star()
second_star()