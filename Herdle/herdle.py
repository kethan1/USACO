import string

# with open("herdle.in") as input_file:
#     correct = [list(input_file.readline().strip()) for _ in range(3)]
#     guess = [list(input_file.readline().strip()) for _ in range(3)]


correct = [list(input()) for _ in range(3)]
guess = [list(input()) for _ in range(3)]


green = yellow = 0
correct_letters = {letter: 0 for letter in list(string.ascii_uppercase)}
guess_letters = correct_letters.copy()
for row_index, row in enumerate(correct):
    for column_index, letter in enumerate(row):
        if guess[row_index][column_index] == letter:
            green += 1
        else:
            correct_letters[letter] += 1
            guess_letters[guess[row_index][column_index]] += 1

for letter, number in correct_letters.items():
    yellow += number if number < guess_letters[letter] else guess_letters[letter]
print(green)
print(yellow)
