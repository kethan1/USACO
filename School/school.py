with open("school.in", "r") as file1:
    classes = [list(map(int, each.strip().split())) for each in file1.readlines()]

initial, min_number, max_number, min_number_dct, max_number_dct = True, 0, 0, {}, {}


def day_str(x):
    return 'Monday' if x == 0 else \
        'Tuesday' if x == 1 else \
        'Wednesday' if x == 2 else \
        'Thursday' if x == 3 else 'Friday'


def subject_str(x):
    return 'History' if x == 0 else \
        'Chemistry' if x == 1 else \
        'Mathematics' if x == 2 else \
        'English' if x == 3 else \
        'Psychology' if x == 4 else 'Biology'


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
