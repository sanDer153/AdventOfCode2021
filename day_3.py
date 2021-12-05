import math


def first_star():
    gamma = ''
    epsilon = ''
    report = []
    with open('day_3_input.txt') as f:
        report = f.readlines()

    for i in range(len(report)):
        report[i] = report[i].rstrip()

    for i in range(len(report[0])):
        amount = 0
        for binary in report:
            amount += int(binary[i])

        if amount > len(report)/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma_value = int(gamma, base=2)
    epsilon_value = int(epsilon, base=2)

    print(gamma_value)
    print(epsilon_value)
    print(int(gamma_value)*int(epsilon_value))


def second_star():
    oxy = []
    co2 = []
    report = []

    with open('day_3_input.txt') as f:
        report = f.readlines()

    for i in range(len(report)):
        report[i] = report[i].rstrip()

    oxy = report[:]
    co2 = report[:]
    i = 0
    while len(oxy) > 1:
        amount = 0
        for binary in oxy:
            amount += int(binary[i])

        if amount >= len(oxy) - amount:
            oxy = list(filter(lambda x: most_common_filter(i, x, '1'), oxy))
        else:
            oxy = list(filter(lambda x: most_common_filter(i, x, '0'), oxy))
        i += 1

    i = 0
    while len(co2) > 1:
        amount = 0
        for binary in co2:
            amount += int(binary[i])

        if amount < len(co2) - amount:
            co2 = list(filter(lambda x: most_common_filter(i, x, '1'), co2))
        else:
            co2 = list(filter(lambda x: most_common_filter(i, x, '0'), co2))
        i += 1

    oxy_rate = int(oxy[0], base=2)
    co2_rate = int(co2[0], base=2)

    print(oxy_rate)
    print(co2_rate)
    print(co2_rate * oxy_rate)


def most_common_filter(i, binary, n):
    return True if binary[i] == n else False


first_star()
second_star()