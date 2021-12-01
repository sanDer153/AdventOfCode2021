def first_star():
    amount = 0
    previous = None
    with open('day_1_input.txt') as f:
        for depth in f:
            depth.strip('\n')
            depth = int(depth)
            if previous is None:
                previous = depth
            if depth > previous:
                amount += 1

            previous = depth

    print(amount)


def second_star():
    amount = 0
    previous = None
    depth_list = []
    with open('day_1_input.txt') as f:
        for depth in f:
            depth.strip()
            depth = int(depth)
            depth_list.append(depth)

    for n in range(len(depth_list)-2):
        depth_sum = depth_list[n] + depth_list[n+1] + depth_list[n+2]
        if previous is None:
            previous = depth_sum
        if depth_sum > previous:
            amount += 1

        previous = depth_sum

    print(amount)

first_star()
second_star()