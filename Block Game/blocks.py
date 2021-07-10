ans = {}
for thing in range(97, 123):
    ans[chr(thing)] = 0

with open("blocks.in", "r") as input_file:
    input_file.readline()

    words = []
    letters = []

    for line in input_file:
        line = line.strip().split(" ")
        words.append(line)
        letters.append([])

for pair in words:
    b = words.index(pair)
    for word in pair:
        for letter in word:
            letters[b].append(letter)

for thing in letters:
    b = letters.index(thing)
    letters[b] = list(set(thing))

for letter_pairs in letters:
    for letter in letter_pairs:
        ans[letter] += 1

with open("blocks.out", "w") as output_file:
    for key, value in ans.items():
        print(value, file=output_file)
