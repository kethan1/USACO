with open("school.in", "r") as file1:
    classes = [list(map(int, each.strip().split())) for each in file1.readlines()]

initial, min_number, max_number, min_number_dct, max_number_dct = True, 0, 0, {}, {}

def day_str(x):
    if x == 0: return 'Monday'
    elif x == 1: return 'Tuesday'
    elif x == 2: return 'Wednesday'
    elif x == 3: return 'Thursday'
    elif x == 4: return 'Friday'

def subject_str(x):
    if x == 0: return 'History'
    elif x == 1: return 'Chemistry'
    elif x == 2: return 'Mathematics'
    elif x == 3: return 'English'
    elif x == 4: return 'Psychology'
    elif x == 5: return 'Biology'

for day in classes:
    for subject in day:
        if initial:
            min_number = subject
            initial = False
        if subject <= min_number:
            min_number = subject
        elif subject >= max_number:
            max_number = subject

for day in classes:
    for subject in day:
        if subject == min_number:
            min_number_dct[subject_str(day.index(subject))] = day_str(classes.index(day))
        elif subject == max_number:
            max_number_dct[subject_str(day.index(subject))] = day_str(classes.index(day))


output_str = ''


for number in max_number_dct:
    output_str += str(max_number_dct[number]) + " - " + number + "; "
output_str += '\n'
for number in min_number_dct:
    output_str += str(min_number_dct[number]) + " - " + number + "; "

with open("school.out", "w") as file2:
    print(output_str, file=file2)
