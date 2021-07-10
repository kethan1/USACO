with open("whatbase.in") as file1:
    k = file1.readline().strip()
    problems = [list(map(int, i.strip().split())) for i in file1.readlines()]


def convert_to_base_10(number, initial_base):
    to_return_number, tmp_loop_number = 0, 0
    for each_letter in str(number)[::-1]:
        to_return_number += (int(each_letter)*(initial_base**tmp_loop_number))
        tmp_loop_number += 1
    return to_return_number


for i in problems:
    x, y = 10, 10
    while True:
        if x < 15001 and y < 15001:
            z = convert_to_base_10(i[0], x)
            a = convert_to_base_10(i[1], y)
            if z < a:
                x += 1
            elif a < z:
                y += 1
            elif a == z:
                with open("whatbase.out", "w") as file1:
                    print(x, y, file=file1)
                    break
