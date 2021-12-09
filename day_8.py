def first_star():
    input_list = []

    with open('day_8_input.txt') as f:
        for line in f:
            line = line.strip()
            input_list.append(line.split("|")[1])

    input_list = [x.split() for x in input_list]

    amount_of_1478 = 0

    for output in input_list:
        for segments in output:
            if len(segments) == 2:
                amount_of_1478 += 1
            elif len(segments) == 3:
                amount_of_1478 += 1
            elif len(segments) == 4:
                amount_of_1478 += 1
            elif len(segments) == 7:
                amount_of_1478 += 1

    print(amount_of_1478)


def second_star():
    input_list = []

    with open('day_8_input.txt') as f:
        for line in f:
            line = line.strip()
            input_list.append(line.split("|"))

    som = 0

    for display in input_list:
        encrypted_list = display[0].split()
        encrypted_list = ["".join(sorted(x)) for x in encrypted_list]
        digits = display[1].split()
        digits = ["".join(sorted(x)) for x in digits]
        solution_key = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}

        len_2 = [x for x in encrypted_list if len(x) == 2]
        len_3 = [x for x in encrypted_list if len(x) == 3]
        len_4 = [x for x in encrypted_list if len(x) == 4]
        len_5 = [x for x in encrypted_list if len(x) == 5]
        len_7 = [x for x in encrypted_list if len(x) == 7]

        solution_key['c'] = solution_key['f'] = set(len_2[0])
        solution_key['a'] = set(len_3[0]) - set(len_2[0])
        solution_key['b'] = solution_key['d'] = set(len_4[0]) - set(len_2[0])
        horizontal_segments = [set(x) - solution_key['c'] for x in len_5 if len(set(x) - solution_key['c']) == 3][0]
        solution_key['d'] = horizontal_segments & solution_key['d']
        solution_key['b'] = solution_key['b'] - solution_key['d']
        solution_key['g'] = horizontal_segments - solution_key['a'] - solution_key['d']
        solution_key['e'] = set(len_7[0]) - solution_key['a'] - solution_key['b'] - solution_key['c'] - solution_key['d'] - solution_key['g']
        digit_2 = [set(x) for x in len_5 if len(set(x) - solution_key['d'] - solution_key['e']) == 3][0]
        solution_key['f'] = solution_key['f'] - digit_2
        solution_key['c'] = solution_key['c'] - solution_key['f']

        for key in solution_key:
            solution_key[key] = "".join(solution_key[key])

        digit_codes = {"".join(sorted(solution_key['a'] + solution_key['b'] + solution_key['c'] + solution_key['e'] + solution_key['f'] + solution_key['g'])): '0',
                        "".join(sorted(solution_key['c'] + solution_key['f'])): '1',
                        "".join(sorted(solution_key['a'] + solution_key['c'] + solution_key['d'] + solution_key['e'] + solution_key['g'])): '2',
                        "".join(sorted(solution_key['a'] + solution_key['c'] + solution_key['d'] + solution_key['f'] + solution_key['g'])): '3',
                        "".join(sorted(solution_key['b'] + solution_key['c'] + solution_key['d'] + solution_key['f'])): '4',
                        "".join(sorted(solution_key['a'] + solution_key['b'] + solution_key['d'] + solution_key['f'] + solution_key['g'])): '5',
                        "".join(sorted(solution_key['a'] + solution_key['b'] + solution_key['d'] + solution_key['e'] + solution_key['f'] + solution_key['g'])): '6',
                        "".join(sorted(solution_key['a'] + solution_key['c'] + solution_key['f'])): '7',
                        "".join(sorted(solution_key['a'] + solution_key['b'] + solution_key['c'] + solution_key['d'] + solution_key['e'] + solution_key['f'] + solution_key['g'])): '8',
                        "".join(sorted(solution_key['a'] + solution_key['b'] + solution_key['c'] + solution_key['d'] + solution_key['f'] + solution_key['g'])): '9',
                        }

        for digit_i in range(len(digits)):
            digits[digit_i] = digit_codes[digits[digit_i]]
        number = int("".join(digits))
        som += number

    print(som)


first_star()
second_star()
