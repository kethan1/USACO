with open('backforth.in') as input_file:
    A = list(map(int, input_file.readline().split()))
    B = list(map(int, input_file.readline().split()))


ans = set()

for bucket1 in A:
    Wed = B + [bucket1]
    for bucket2 in Wed:
        Thurs = A.copy()
        if bucket1 != bucket2:
            Thurs.append(bucket2)
            Thurs.remove(bucket1)
        for bucket3 in Thurs:
            Fri = Wed + [bucket3]
            Fri.remove(bucket2)
            for bucket4 in Fri:
                ans.add(bucket1 - bucket2 + bucket3 - bucket4)

with open('backforth.out', 'w') as output_file:
    output_file.write(str(len(ans)))
