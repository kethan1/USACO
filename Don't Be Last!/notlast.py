with open("notlast.in", "r") as input_file:
    input_file.readline()
    input_dct = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}
    for line in input_file:
        cow_name, milk_produced = line.split()
        input_dct[cow_name] += int(milk_produced)

with open("notlast.out", "w") as output_file:
    mins = sorted(set(input_dct.values()))
    if len(mins) > 1:
        if list(input_dct.values()).count(mins[1]) == 1:
            print({value: key for key, value in input_dct.items()}[mins[1]], file=output_file)
        else:
            print("Tie", file=output_file)
    else:
        print("Tie", file=output_file)
