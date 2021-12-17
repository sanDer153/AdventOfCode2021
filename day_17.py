def second_star():
    amount = 0
    for x_velocity in range(231):
        for y_velocity in range(-100, 100):
            if simulate(x_velocity, y_velocity):
                amount += 1

    print(amount)


def simulate(x_velocity, y_velocity):
    x_pos = 0
    y_pos = 0
    while y_pos > -100:
        x_pos += x_velocity
        y_pos += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1

        if 201 <= x_pos <= 230 and -99 <= y_pos <= -65:
            return True

    return False


second_star()