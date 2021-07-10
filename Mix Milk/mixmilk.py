file = open("mixmilk.in", "r")

a = file.readline().strip().split()
b = file.readline().strip().split()
c = file.readline().strip().split()

b1c = int(a[0])
b1a = int(a[1])
b2c = int(b[0])
b2a = int(b[1])
b3c = int(c[0])
b3a = int(c[1])
cycles = 0
nextob = 1
minus = 1

file.close()

while cycles < 101:
    cycles+=1
    if nextob == 1:
        if b1a+b2a > b2c:
            while True:
                if (b1a-minus)+b2a <= b2c:
                    b2a = (b1a-minus)+b2a
                    b1a = b1a-(b1a-minus)
                    break
                else:
                    minus+=1
        else:
            b2a = b2a+b1a
            b1a = 0
        nextob +=1
        minus = 1

    
    if nextob == 2:
        if b2a+b3a > b3c:
            while True:
                if (b2a-minus)+b3a <= b3c:
                    b3a = (b2a-minus)+b3a
                    b2a = b2a-(b2a-minus)
                    break
                else:
                    minus+=1
        else:
            b3a = b3a+b2a
            b2a = 0
        nextob +=1
        minus = 1
    
    if nextob == 3:
        if b3a+b1a > b1c:
            while True:
                if (b3a-minus)+b1a <= b1c:
                    b1a = (b3a-minus)+b1a
                    b3a = b3a-(b3a-minus)
                    break
                else:
                    minus+=1
        else:
            b1a = b1a+b3a
            b3a = 0
        nextob = 1
        minus = 1

file2 = open("mixmilk.out", "w")

print(b1a, b2a, b3a, sep="\n", file=file2)

file2.close()