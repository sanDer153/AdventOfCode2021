start_polymer = 'OFSVVSFOCBNONHKFHNPK'
insertions = {}

with open('day_14_input.txt') as f:
    for line in f:
        insertions[line.strip().split(' -> ')[0]] = line.strip().split(' -> ')[1]


def first_star():
    polymer = start_polymer
    for run in range(10):
        number_of_insertions = len(polymer) - 1
        i = 0
        while i < number_of_insertions:
            polymer = polymer[:2 * i + 1] + insertions[polymer[2 * i: 2 * i + 2]] + polymer[2 * i + 1:]
            i += 1

    most_common = 0
    least_common = len(polymer)

    for letter in polymer:
        if polymer.count(letter) < least_common:
            least_common = polymer.count(letter)
        if polymer.count(letter) > most_common:
            most_common = polymer.count(letter)

    print(most_common - least_common)


def second_star():
    polymer_pairs = {}
    transitions = {}
    letter_count = {}
    for polymer_pair in insertions:
        polymer_pairs[polymer_pair] = 0
        transitions[polymer_pair] = [polymer_pair[0]+insertions[polymer_pair], insertions[polymer_pair]+polymer_pair[1]]

    for i in range(len(start_polymer) - 1):
        polymer_pairs[start_polymer[i : i+2]] += 1

    for run in range(40):
        new_polymer_pairs = polymer_pairs.copy()
        for polymer_pair in polymer_pairs:
            new_polymer_pairs[transitions[polymer_pair][0]] += polymer_pairs[polymer_pair]
            new_polymer_pairs[transitions[polymer_pair][1]] += polymer_pairs[polymer_pair]
            new_polymer_pairs[polymer_pair] -= polymer_pairs[polymer_pair]
            if new_polymer_pairs[polymer_pair] < 0:
                new_polymer_pairs[polymer_pair] = 0
        polymer_pairs = new_polymer_pairs

    for polymer_pair in polymer_pairs:
        if polymer_pair[0] in letter_count:
            letter_count[polymer_pair[0]] += polymer_pairs[polymer_pair]
        else:
            letter_count[polymer_pair[0]] = polymer_pairs[polymer_pair]

        if polymer_pair[1] in letter_count:
            letter_count[polymer_pair[1]] += polymer_pairs[polymer_pair]
        else:
            letter_count[polymer_pair[1]] = polymer_pairs[polymer_pair]

    letter_count['O'] += 1
    letter_count['K'] += 1
    for letter in letter_count:
        letter_count[letter] //= 2

    print(max(letter_count.values())-min(letter_count.values()))


first_star()
second_star()