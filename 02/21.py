# Read input
with open("input.txt", "r") as f:
    tournament = f.readlines()

LOSS = 'loss'
DRAW = 'draw'
WIN = 'win'
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

score = 0
shapes = {ROCK: ['A', 'X'], PAPER: ['B', 'Y'], SCISSORS: ['C', 'Z']}
shape_scores = {ROCK: 1, PAPER: 2, SCISSORS: 3}
outcome_scores = {LOSS: 0, DRAW: 3, WIN: 6}


def get_shape(shape_letter):
    for shape in shapes:
        if shape_letter in shapes[shape]:
            return shape


def get_round_score(round):
    elf_shape = get_shape(round[0])
    my_shape = get_shape(round[2])

    if elf_shape == my_shape:
        return outcome_scores[DRAW] + shape_scores[my_shape]
    if elf_shape == ROCK:
        if my_shape == PAPER:
            return outcome_scores[WIN] + shape_scores[my_shape]
        elif my_shape == SCISSORS:
            return outcome_scores[LOSS] + shape_scores[my_shape]
    if elf_shape == PAPER:
        if my_shape == ROCK:
            return outcome_scores[LOSS] + shape_scores[my_shape]
        elif my_shape == SCISSORS:
            return outcome_scores[WIN] + shape_scores[my_shape]
    if elf_shape == SCISSORS:
        if my_shape == PAPER:
            return outcome_scores[LOSS] + shape_scores[my_shape]
        elif my_shape == ROCK:
            return outcome_scores[WIN] + shape_scores[my_shape]


for round in tournament:
    score += get_round_score(round)

print(score)
