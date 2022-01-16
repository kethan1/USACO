with open("word.in") as input_file:
    N, K = map(int, input_file.readline().split())
    essay = input_file.readline().strip().split()

output_lines = [""]
for word in essay:
    if len(output_lines[-1].replace(" ", "")) + len(word) <= K:
        output_lines[-1] += word if output_lines[-1] == "" else f" {word}"
    else:
        output_lines.append(word)

with open("word.out", "w") as output_file:
    print(*output_lines, file=output_file, sep="\n")
