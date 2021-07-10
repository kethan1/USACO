with open("water.in", "r") as file1:
    inputList = [line.strip() for line in file1]
with open("water.out", "w") as file2:
    for each in [round((2/3*3.14*(int(each, 2)**3))/1000) for each in inputList]:
        print(each, file=file2)
