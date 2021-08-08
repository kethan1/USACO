with open("water.in", "r") as input_file:
    input_list = [line.strip() for line in input_file]
with open("water.out", "w") as output_file:
    for binary_diameter in input_list:
        print(round((2/3 * 3.14 * (int(binary_diameter, 2) ** 3)) / 1000), file=output_file)
