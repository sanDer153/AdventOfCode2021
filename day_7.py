# starting_values = [16,1,2,0,4,2,7,1,2,14]
#
#
with open('day_7_input.txt') as f:
    starting_values = list(map(int, f.readline().split(',')))


def first_star():
    gemiddelde = sum(starting_values)//len(starting_values)
    afwijking = [abs(gemiddelde - x) for x in starting_values]

    if sum([abs(gemiddelde - 1 - x) for x in starting_values]) < sum(afwijking):
        gemiddelde -= 1
        afwijking = [abs(gemiddelde - x) for x in starting_values]
        while sum([abs(gemiddelde - 1 - x) for x in starting_values]) < sum(afwijking):
            gemiddelde -= 1
            afwijking = [abs(gemiddelde - x) for x in starting_values]
    elif sum([abs(gemiddelde + 1 - x) for x in starting_values]) < sum(afwijking):
        gemiddelde += 1
        afwijking = [abs(gemiddelde - x) for x in starting_values]
        while sum([abs(gemiddelde + 1 - x) for x in starting_values]) < sum(afwijking):
            gemiddelde += 1
            afwijking = [abs(gemiddelde - x) for x in starting_values]

    print(sum(afwijking))


def second_star():
    gemiddelde = sum(starting_values) // len(starting_values)
    afwijking = [abs(gemiddelde - x) * (abs(gemiddelde - x) + 1) // 2 for x in starting_values]

    if sum([abs(gemiddelde - 1 - x) * (abs(gemiddelde - 1 - x) + 1) // 2 for x in starting_values]) < sum(afwijking):
        gemiddelde -= 1
        afwijking = [abs(gemiddelde - x) * (abs(gemiddelde - x) + 1) // 2 for x in starting_values]
        while sum([abs(gemiddelde - 1 - x) * (abs(gemiddelde - 1 - x) + 1) // 2 for x in starting_values]) < sum(afwijking):
            gemiddelde -= 1
            afwijking = [abs(gemiddelde - x) * (abs(gemiddelde - x) + 1) // 2 for x in starting_values]
    elif sum([abs(gemiddelde + 1 - x) * (abs(gemiddelde + 1 - x) + 1) // 2 for x in starting_values]) < sum(afwijking):
        gemiddelde += 1
        afwijking = [abs(gemiddelde - x) * (abs(gemiddelde - x) + 1) // 2 for x in starting_values]
        while sum([abs(gemiddelde + 1 - x) * (abs(gemiddelde + 1 - x) + 1) // 2 for x in starting_values]) < sum(afwijking):
            gemiddelde += 1
            afwijking = [abs(gemiddelde - x) * (abs(gemiddelde - x) + 1) // 2 for x in starting_values]

    print(sum(afwijking))


first_star()
second_star()