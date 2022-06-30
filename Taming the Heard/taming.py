with open("taming.in") as input_file:
    N = int(input_file.readline())
    days = list(map(int, input_file.readline().split()))

for index, day in list(enumerate(days))[1:]:
    if days[index - 1] == -1 and day != -1:
        for day_num, counter in enumerate(range(index - 1, index - day - 1, -1)):
            if days[counter] != -1:
                break
            days[counter] = day - (day_num + 1)


def is_pattern_valid(days):
    return not any(day not in [0, -1] and days[index + 1] not in [0, -1] and day + 1 != days[index + 1] for index, day in enumerate(days[:-1]))


with open("taming.out", "w") as output_file:
    print(days)
    if days[0] in [0, -1] and is_pattern_valid(days):
        days[0] = 0
        min_breakouts = days.count(0)
        max_breakouts = min_breakouts + days.count(-1)
        print(min_breakouts, max_breakouts, file=output_file)
    else:
        print(-1, file=output_file)
