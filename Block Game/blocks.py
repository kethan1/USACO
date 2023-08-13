import string
from collections import Counter


with open("blocks.in", "r") as input_file:
    N = int(input_file.readline())
    words = list(map(lambda line: line.strip().split(), input_file.readlines()))


min_letters = {chr(char): 0 for char in range(ord("a"), ord("z") + 1)}
empty = {chr(char): 0 for char in range(ord("a"), ord("z") + 1)}

for (word1, word2) in words:
    word1_freqs = {**empty, **Counter(word1)}
    word2_freqs = {**empty, **Counter(word2)}
    for letter in string.ascii_lowercase:
        min_letters[letter] += max(word1_freqs[letter], word2_freqs[letter])

with open("blocks.out", "w") as output_file:
    print(*min_letters.values(), file=output_file, sep="\n")
