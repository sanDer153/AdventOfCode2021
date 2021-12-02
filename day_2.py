def first_star():
    horizontal = 0
    depth = 0
    with open('day_2_input.txt') as f:
        for cmd in f:
            cmd.strip()
            cmd_list = cmd.split(' ')
            cmd_list[1] = int(cmd_list[1])

            if cmd_list[0] == "forward":
                horizontal += cmd_list[1]
            elif cmd_list[0] == "down":
                depth += cmd_list[1]
            elif cmd_list[0] =="up":
                depth -= cmd_list[1]

        print(horizontal)
        print(depth)
        print(horizontal*depth)


def second_star():
    horizontal = 0
    depth = 0
    aim = 0
    with open('day_2_input.txt') as f:
        for cmd in f:
            cmd.strip()
            cmd_list = cmd.split(' ')
            cmd_list[1] = int(cmd_list[1])

            if cmd_list[0] == "forward":
                horizontal += cmd_list[1]
                depth += aim*cmd_list[1]
            elif cmd_list[0] == "down":
                aim += cmd_list[1]
            elif cmd_list[0] =="up":
                aim -= cmd_list[1]

        print(horizontal)
        print(depth)
        print(horizontal*depth)


first_star()
second_star()