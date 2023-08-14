import math


N = int(input())
conditions = [input().split() for _ in range(N)]
greater_conditions = [int(c[1]) for c in conditions if c[0] == "G"]
less_conditions = [int(c[1]) for c in conditions if c[0] == "L"]

bessie_positions = greater_conditions + less_conditions

min_liars = math.inf
for position in bessie_positions:
    liars = 0
    for condition in conditions:
        if condition[0] == "G":
            if position < int(condition[1]):
                liars += 1
        elif condition[0] == "L":
            if position > int(condition[1]):
                liars += 1
    min_liars = min(min_liars, liars)

print(min_liars)
