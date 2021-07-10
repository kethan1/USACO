file = open("bucket_list.in", "r")
numberofcows = file.readline().strip()
data = []
for line in file:
    start,end,bucket = line.split()
    data.append([int(start), int(end), int(bucket)])
file.close()
    
maximum_time = sorted(data, reverse = True, key = lambda x: x[2])[0][2]

bucketlist = []
for time in range(1, maximum_time+1):
    numberofbuckets = 0
    for info in data:
        if info[0]<=time and time<=info[1]:
            numberofbuckets+=info[2]
    bucketlist.append(numberofbuckets)
    
file2 = open("ans.out", "w")
print(max(bucketlist), file=file2)
file2.close()