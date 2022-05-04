import itertools

with open("tttt.in") as input_file:
    board = [list(line.strip()) for line in input_file]
    cows = {cow for line in board for cow in line}


def equal_to(letters, *lst):
    return (
        sum(lst.count(letter) for letter in letters) == len(lst)
        and min(lst.count(letter) for letter in letters) > 0
    )


def check_board(board, letters):
    return (
        equal_to(letters, *board[0])
        or equal_to(letters, *board[1])
        or equal_to(letters, *board[2])
        or equal_to(letters, board[0][0], board[1][0], board[2][0])
        or equal_to(letters, board[0][1], board[1][1], board[2][1])
        or equal_to(letters, board[0][2], board[1][2], board[2][2])
        or equal_to(letters, board[0][0], board[1][1], board[2][2])
        or equal_to(letters, board[0][2], board[1][1], board[2][0])
    )


individual_winners = sum(check_board(board, [cow]) for cow in cows)
team_winners = sum(check_board(board, team) for team in itertools.combinations(cows, 2))

with open("tttt.out", "w") as output_file:
    print(individual_winners, file=output_file)
    print(team_winners, file=output_file)
