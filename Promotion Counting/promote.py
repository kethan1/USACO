with open("promote.in") as input_file:
    input_lst = [[*map(int, line.split())] for line in input_file]

promotions = [
    promotion[1] - promotion[0] for promotion in input_lst
]
output = []
for promotion in promotions[::-1]:
    output.append(sum([]))

with open("promote.out", "w") as output_file:
    for promotion in promotions:
        print(promotion, file=output_file)

# print(input_lst)
