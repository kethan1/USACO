with open("shell.in") as input_file:
    input_file.readline()
    switches_and_guesses = [list(map(int, line.strip().split())) for line in input_file]

shells = {
    1: 0,
    2: 0,
    3: 0
}

correct_guesses = [0, 0, 0]

for shell_start in range(1, 4):
    shells[shell_start] = 1

    for move in switches_and_guesses:
        shells[move[0]], shells[move[1]] = shells[move[1]], shells[move[0]]
        correct_guesses[shell_start - 1] += shells[move[2]]

    # converts all values to 0
    shells = shells.fromkeys(shells, 0)

with open("shell.out", "w") as output_file:
    output_file.write(str(max(correct_guesses)))
