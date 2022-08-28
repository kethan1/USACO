cow_states = {}
crosses = 0

with open("crossroad.in") as input_file:
    N = int(input_file.readline())
    for line in input_file:
        cow_id, state = map(int, line.split())
        if cow_id not in cow_states:
            cow_states[cow_id] = state
        elif cow_states[cow_id] != state:
            crosses += 1
            cow_states[cow_id] = state

with open("crossroad.out", "w") as output_file:
    print(crosses, file=output_file)
