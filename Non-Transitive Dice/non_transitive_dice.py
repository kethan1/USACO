T = int(input())
test_cases = []
for _ in range(T):
    full_line = list(map(int, input().split()))
    test_cases.append([full_line[:4], full_line[4:]])


possible_dice = [
    [n1, n2, n3, n4]
    for n1 in range(1, 11)
    for n2 in range(1, 11)
    for n3 in range(1, 11)
    for n4 in range(1, 11)
]


def wins(a, b):
    wins = 0
    loses = 0
    for side in a:
        for side2 in b:
            if side > side2:
                wins += 1
            elif side < side2:
                loses += 1
    return wins > loses


for test_case in test_cases:
    a, b = test_case
    for c in possible_dice:
        if (wins(a, b) and wins(b, c) and wins(c, a)) or (wins(c, b) and wins(b, a) and wins(a, c)):
            print("yes")
            break
    else:
        print("no")
