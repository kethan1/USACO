def repeat_chars(string, k):
    return ''.join([c * k for c in string])


output = ""
with open("cowsignal.in") as input_file:
    M, N, K = map(int, input_file.readline().strip().split())
    for line in input_file:
        output += (repeat_chars(line.strip(), K) + "\n") * K

with open("cowsignal.out", "w") as output_file:
    output_file.write(output)
