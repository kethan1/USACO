with open('backforth.in', 'r') as file1:
    A = list(map(int, file1.readline().strip().split()))
    B = list(map(int, file1.readline().strip().split()))


ans_list = []

Tue = A.copy()
for bucket1 in Tue:
    Wed = B.copy() + [bucket1]
    for bucket2 in Wed:
        if bucket1 == bucket2:
            Thurs = Tue.copy()
        else:
            Thurs = Tue.copy() + [bucket2]
            Thurs.remove(bucket1)
        for bucket3 in Thurs:
            Fri = Wed.copy() + [bucket3]
            Fri.remove(bucket2)
            for bucket4 in Fri:
                x = bucket1-bucket2+bucket3-bucket4
                if x not in ans_list:
                    ans_list.append(x)


with open('backforth.out', 'w') as file2:
    print(len(ans_list), file=file2)