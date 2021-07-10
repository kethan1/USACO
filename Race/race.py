data = []

with open('race.in') as input_file:
    for line in input_file.readlines():
        data.append(list(map(int, line.strip().split())))

output = ''

for each in data:
    x = each[0:3]
    won_person = x.index(min(x))
    if won_person == 0:
        won_person_letter = 'A'
    elif won_person == 1:
        won_person_letter = 'B'
    elif won_person == 2:
        won_person_letter = 'C'
    output += won_person_letter+' '+str(round(each[3]/each[won_person]))+'\n'

with open('race.out', 'w') as file2:
    print(output, file=file2)
