with open("squares.in", "r") as file1:
    input_lst = [int(i.strip()) for i in file1.readlines()]
with open("squares.out", "w") as file2:
    print(int(((int(input_lst[0]/input_lst[2])*input_lst[2])*(int(input_lst[1]/input_lst[2])*input_lst[2]))/(input_lst[2]*input_lst[2])), "\n"+str((input_lst[0]*input_lst[1])-((int(input_lst[0]/input_lst[2])*input_lst[2])*(int(input_lst[1]/input_lst[2])*input_lst[2]))), file=file2)