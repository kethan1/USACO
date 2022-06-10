with open("race.in") as input_file:
    K, N = map(int, input_file.readline().split())
    Xs = list(map(int, input_file.readlines()))


def summation(start, stop=0):
    return sum(range(stop, start+1))


outputs = []
for X in Xs:
    time = speed = position = 0
    while position < K:
        if K - position - summation(speed + 1, X) >= 0:
            speed += 1
        elif speed > 0 and K - position - summation(speed, X) < 0:
            speed -= 1
        position += speed
        time += 1
    outputs.append(time)

with open("race.out", "w") as input_file:
    print(*outputs, sep="\n", file=input_file)
