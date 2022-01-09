import os
from collections import deque

cows = []
years_of_cows = {"Bessie": "Ox"}

# with open("year_of_the_cow.in") as input_file:
#     input_file.readline()
#     for line in input_file:
#         split_line = line.split()
#         years_of_cows[split_line[0]] = split_line[4]
#         cows.append([split_line[0], split_line[3], split_line[4], split_line[7]])

N = int(input())
for _ in range(N):
    line = input()
    split_line = line.split()
    years_of_cows[split_line[0]] = split_line[4]
    cows.append([split_line[0], split_line[3], split_line[4], split_line[7]])


def move_portion_to_end(ending_year):
    years_copy = deque(years.copy())
    years_copy.rotate(len(years[years.index(ending_year): -1]))
    return list(years_copy)


def move_portion_to_start(starting_year):
    years_copy = deque(years.copy())
    years_copy.rotate(-len(years[:years.index(starting_year)]))
    return list(years_copy)


years = [
    "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey",
    "Rooster", "Dog", "Pig", "Rat", "Ox",
]

ages = {
    "Bessie": 0
}

for cow in cows:
    if cow[1] == "previous":
        years_moved = move_portion_to_end(years_of_cows[cow[3]])
        if cow[2] == years_of_cows[cow[3]]:
            ages[cow[0]] = ages[cow[3]] - 12
        else:
            ages[cow[0]] = ages[cow[3]] - 11 + years_moved.index(cow[2])
    elif cow[1] == "next":
        years_moved = move_portion_to_start(years_of_cows[cow[3]])
        if cow[2] == years_of_cows[cow[3]]:
            ages[cow[0]] = ages[cow[3]] + 12
        else:
            ages[cow[0]] = ages[cow[3]] + years_moved.index(cow[2])
    if cow[0] == "Elsie":
        break

print(abs(ages["Elsie"]))
