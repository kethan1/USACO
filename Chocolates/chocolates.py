with open("chocolates.in", "r") as file1:
    times, chocolates = int(file1.readline().strip()), int(file1.readline().strip())
    
with open("chocolates.out", "w") as file2: print(sum([(i+1)*chocolates for i in range(0, times)]), file=file2)