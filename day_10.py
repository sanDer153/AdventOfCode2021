BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}
VALUES = {')': 3, ']': 57, '}': 1197, '>': 25137}
VALUES_2 = {')': 1, ']': 2, '}': 3, '>': 4}
input_list = []
incomplete_lines = []
with open('day_10_input.txt') as f:
    input_list = f.readlines()


def first_star():
    error_score = 0
    for line in input_list:
        line = line.strip()
        incomplete_lines.append(line)
        stack = []
        for bracket in line:
            if bracket in BRACKETS:
                stack.append(bracket)
            else:
                if BRACKETS[stack.pop()] != bracket:
                    error_score += VALUES[bracket]
                    if line in incomplete_lines:
                        incomplete_lines.remove(line)


    print(error_score)


def second_star():
    scores = []
    for line in incomplete_lines:
        score = 0
        stack = []
        for bracket in line:
            if bracket in BRACKETS:
                stack.append(bracket)
            else:
                stack.pop()

        while len(stack) != 0:
            score *= 5
            score += VALUES_2[BRACKETS[stack.pop()]]

        scores.append(score)
    scores.sort()
    print(scores[(len(scores)-1)//2])


first_star()
second_star()