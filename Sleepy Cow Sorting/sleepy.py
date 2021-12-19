with open("sleepy.in") as input_file:
    input_file.readline()
    cows = list(map(int, input_file.readline().split()))

def is_list_sorted(lst):
    return all(elem >= lst[index] for index, elem in enumerate(lst[1:]))

t = 0
sorted_cows = cows.copy()
for cow in cows:
    if is_list_sorted(sorted_cows):
        break

    if cow > sorted_cows[-1]:
        sorted_cows.remove(cow)
        sorted_cows.append(cow)
    else:
        i = -1
        n = sorted_cows[i]
        while cow < sorted_cows[i]:
            i -= 1
            if i < 0 or n < sorted_cows[i]:
                break
        sorted_cows.remove(cow)
        sorted_cows.insert(i, cow)
    t += 1

with open("sleepy.out", "w") as output_file:
    output_file.write(str(t))
