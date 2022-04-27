# with open("cownditioning.in") as input_file:
#     N = int(input_file.readline())
#     preferred = list(map(int, input_file.readline().split()))
#     current = list(map(int, input_file.readline().split()))

N = int(input())
preferred = list(map(int, input().split()))
current = list(map(int, input().split()))

iters = 0
differences = [num - current[index] for index, num in enumerate(preferred)]
prev_direction = 0
direction = 0
for index, dif in enumerate(differences):
    direction = 1 if dif > 0 else -1
    iters += abs(dif)
    if index != 0 and prev_direction == direction:
        iters -= min(abs(dif), abs(differences[index - 1]))
    prev_direction = direction

print(iters)
