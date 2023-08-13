with open("diamond.in") as input_file:
    N, K = map(int, input_file.readline().split())
    sizes = list(map(lambda line: int(line.strip()), input_file.readlines()))


min_elem = min(sizes)
max_elem = max(sizes)


def elems_in_range(lst, start, end):
    return sum(start <= elem <= end for elem in lst)


displayable = 0

for start in range(min_elem, max_elem + 1):
    displayable = max(displayable, elems_in_range(sizes, start, start + K))


with open("diamond.out", "w") as output_file:
    print(displayable, file=output_file)
