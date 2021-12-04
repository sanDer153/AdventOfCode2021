picked_numbers = [17,25,31,22,79,72,58,47,62,50,30,91,11,63,66,83,33,75,44,18,56,81,32,46,93,13,41,65,14,95,19,38,8,35,52,7,12,70,84,23,4,42,90,60,6,40,97,16,27,86,5,48,54,64,29,67,26,89,99,53,34,0,57,3,92,37,59,9,21,78,51,80,73,82,76,28,88,96,45,69,98,1,2,71,68,49,36,15,55,39,87,77,74,94,61,85,10,43,20,24]
# picked_numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]


class BingoCard:

    card_matrix = [[]]
    dimension = 0
    still_playing = True

    def __init__(self, input_list):
        self.card_matrix = [list(map(int, row.split())) for row in input_list]
        self.dimension = len(self.card_matrix)
        self.still_playing = True

    def check_number(self, number):
        for row in range(self.dimension):
            for col in range(self.dimension):
                if self.card_matrix[row][col] == number:
                    self.card_matrix[row][col] = -1

    def has_won(self):
        for n in range(self.dimension):
            if self.card_matrix[n].count(-1) == self.dimension or [self.card_matrix[x][n] for x in range(self.dimension)].count(-1) == self.dimension:
                return True

        return False

    def calc_score(self, last_number):
        score = 0
        for row in range(self.dimension):
            for col in range(self.dimension):
                if not self.card_matrix[row][col] == -1:
                    score += self.card_matrix[row][col]

        return score * last_number


def first_star():
    # input_list = ['22 13 17 11  0', '8  2 23  4 24', '21  9 14 16  7', '6 10  3 18  5', '1 12 20 15 19', '', '3 15  0  2 22', '9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6', '', '14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', '2  0 12  3  7']
    bingo_cards = []
    with open('day_4_input.txt') as f:
        input_list = f.readlines()

    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()
    split_input_list = [input_list[6*x: 6*x+5] for x in range((len(input_list)+1)//6)]

    for card in split_input_list:
        bingo_cards.append(BingoCard(card))

    game_over = False
    last_number = -1
    while not game_over and last_number < len(picked_numbers):
        last_number += 1
        for bingo_card in bingo_cards:
            bingo_card.check_number(picked_numbers[last_number])
            if bingo_card.has_won():
                game_over = True
                print(bingo_card.calc_score(picked_numbers[last_number]))


def second_star():
    # input_list = ['22 13 17 11  0', '8  2 23  4 24', '21  9 14 16  7', '6 10  3 18  5', '1 12 20 15 19', '', '3 15  0  2 22', '9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6', '', '14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', '2  0 12  3  7']
    bingo_cards = []
    with open('day_4_input.txt') as f:
        input_list = f.readlines()

    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()
    split_input_list = [input_list[6*x: 6*x+5] for x in range((len(input_list)+1)//6)]

    for card in split_input_list:
        bingo_cards.append(BingoCard(card))

    game_over = False
    last_number = -1
    while not game_over and last_number < len(picked_numbers):
        last_number += 1
        bingo_cards = [bingo_card for bingo_card in bingo_cards if bingo_card.still_playing]
        for bingo_card in bingo_cards:
            bingo_card.check_number(picked_numbers[last_number])
            if bingo_card.has_won():
                bingo_card.still_playing = False
                if len(bingo_cards) == 1:
                    game_over = True
                    print(bingo_card.calc_score(picked_numbers[last_number]))


first_star()
second_star()