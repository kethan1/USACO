# with open("just_stalling.in") as file_input:
#     N = int(file_input.readline())
#     cow_heights = list(map(int, file_input.readline().split()))
#     stall_heights = list(map(int, file_input.readline().split()))

N, cow_heights, stall_heights = int(input()), list(map(int, input().split())), list(map(int, input().split()))

stalls_taken, answer = 0, 1
for cow in sorted(cow_heights, reverse=True):
    answer *= len([stall_height for stall_height in stall_heights if stall_height >= cow])-stalls_taken
    stalls_taken += 1
print(answer)
