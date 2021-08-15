import itertools

with open("hps.in") as input_file:
    input_file.readline()
    moves = [[*map(int, line.strip().split())] for line in input_file]


def won(moves):
    possibilites = []
    for permutation in itertools.permutations(["R", "P", "S"]):
        games_won = 0
        for move in moves:
            move1L, move2L = permutation[move[0] - 1], permutation[move[1] - 1]
            if (move1L == "R" and move2L == "S") or (move1L == "S" and move2L == "P") or (move1L == "P" and move2L == "R"):
                games_won += 1
        possibilites.append(games_won)
    return max(possibilites)


with open("hps.out", "w") as output_file:
    print(won(moves), file=output_file)
