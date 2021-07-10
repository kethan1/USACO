with open("uddered_but_not_herd.in") as file_in:
    cowphabet = file_in.readline()
    heard = list(file_in.readline())

# cowphabet = input()
# heard = list(input())

repetitions, index = 1, 0
while heard:
    for letter in cowphabet:
        if heard[0] == letter: 
            heard.remove(letter)
            if heard == []: break
    repetitions+=1

print(repetitions)
