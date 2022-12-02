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
shapes = {ROCK: 'A', PAPER: 'B', SCISSORS: 'C'}
outcomes = {LOSS: 'X', DRAW: 'Y', WIN: 'Z'}
shape_scores = {ROCK: 1, PAPER: 2, SCISSORS: 3}
outcome_scores = {LOSS: 0, DRAW: 3, WIN: 6}


def get_elf_shape(shape_letter):
    for shape in shapes:
        if shape_letter == shapes[shape]:
            return shape


def get_outcome(outcome_letter):
    for outcome in outcomes:
        if outcome_letter == outcomes[outcome]:
            return outcome


def get_my_shape(elf_shape, outcome):
    if outcome == DRAW:
        return elf_shape
    if outcome == LOSS:
        if elf_shape == ROCK:
            return SCISSORS
        elif elf_shape == PAPER:
            return ROCK
        elif elf_shape == SCISSORS:
            return PAPER
    if outcome == WIN:
        if elf_shape == ROCK:
            return PAPER
        elif elf_shape == PAPER:
            return SCISSORS
        elif elf_shape == SCISSORS:
            return ROCK


def get_round_score(round):
    elf_shape = get_elf_shape(round[0])
    outcome = get_outcome(round[2])
    my_shape = get_my_shape(elf_shape, outcome)

    return outcome_scores[outcome] + shape_scores[my_shape]


for round in tournament:
    score += get_round_score(round)

print(score)
