with open("houses.in", "r") as file1: n, m, colors, answer, x, patterns = int(file1.readline()), int(file1.readline()), [i.strip() for i in file1.readlines()], 0, 0, []
for i in colors:
    try:
        for d in range(1, m+1):
            if i == colors[x+d]: 
                if sorted([x, x+d]) not in patterns: answer+=1;patterns.append(sorted([x,x+d]))
    except:
        if len(colors) == colors.index(colors[x]):
            for d in range(0, m):
                if i == colors[d]:
                    if sorted([x, d]) not in patterns: answer+=1; patterns.append(sorted([x,d]))
        else:
            for d in range(0, m):
                if i == colors[d]: 
                    if sorted([x, d]) not in patterns: answer+=1; patterns.append(sorted([x,d]))
            
    x+=1
with open("houses.out", "w") as file2: print(answer, file=file2)
