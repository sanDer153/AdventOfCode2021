starting_values = []
fish = []


with open('day_6_input.txt') as f:
    starting_values = list(map(int, f.readline().split(',')))


def new_fish():
    fish.append(LanternFish(9))


class LanternFish:
    clock_status = 0

    def __init__(self, clock_status):
        self.clock_status = clock_status

    def day_passed(self):
        if self.clock_status == 0:
            self.clock_status = 6
            new_fish()
        else:
            self.clock_status -= 1


def first_star():
    for clock in starting_values:
        fish.append(LanternFish(clock))

    for day in range(80):
        for lantern_fish in fish:
            lantern_fish.day_passed()

    print(len(fish))


def second_star():
    fase_group_amount = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for clock in starting_values:
        fase_group_amount[clock] += 1

    for day in range(256):
        amount_in_zero = fase_group_amount[0]
        for fase_group in range(8):
            fase_group_amount[fase_group] = fase_group_amount[fase_group + 1]

        fase_group_amount[6] += amount_in_zero
        fase_group_amount[8] = amount_in_zero

    print(sum(fase_group_amount.values()))


first_star()
second_star()