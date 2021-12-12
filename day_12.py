ACCEPT = 0
ABANDON = 1
CONTINUE = 2

connections = {}

with open('day_12_input.txt') as f:
    for line in f:
        line = line.strip()
        nodes = line.split('-')
        for node in nodes:
            if node not in connections:
                connections[node] = {x for x in nodes if x != node}
            else:
                connections[node].update({x for x in nodes if x != node})


def examine(partial_solution):
    double_small_cave = ''
    for node in partial_solution:
        if node.islower() and partial_solution.count(node) == 2 and node != 'start' and node != 'end':
            double_small_cave = node

    if any(partial_solution.count(x) > 1 and x.islower() and x != double_small_cave for x in partial_solution):
        return ABANDON
    elif partial_solution[-1] == 'end':
        return ACCEPT
    else:
        return CONTINUE


def extend(partial_solution):
    return [partial_solution + [x] for x in connections[partial_solution[-1]]]


def solve(solution, partial_solution):
    exam = examine(partial_solution)
    if exam == ACCEPT:
        solution.append(partial_solution)
    elif exam == CONTINUE:
        for p in extend(partial_solution):
            solve(solution, p)


def first_star():
    paths = []
    solve(paths, ['start'])
    print(len(paths))


first_star()