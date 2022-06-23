with open("family.in") as input_file:
    rel_num, cow_a, cow_b = input_file.readline().split()
    relations = [line.strip().split() for line in input_file]


def mother(cow):
    for relation in relations:
        mother, child = relation
        if child == cow:
            return mother
    return None


def direct_anc_dist(cow, cow2):
    dist = 0
    while cow2 is not None:
        if cow == cow2:
            return dist
        cow2 = mother(cow2)
        dist += 1
    return -1


da = 0
cow = cow_a
while cow is None and direct_anc_dist(cow, cow_b) == -1:
    cow = mother(cow)
    da += 1

relationship = ""
if cow is None:
    relationship = "NOT RELATED"
else:
    db = direct_anc_dist(cow, cow_b)
    if da > 1 and db > 1:
        relationship = "COUSINS"
    elif da == 1 and db == 1:
        relationship = "SIBLINGS"
    else:
        if da > db:
            da, db = db, da
            cow_b, cow_a = cow_a, cow_b
        relationship = f"{cow_a} is the "

        for _ in range(db - 2):
            relationship += "great-"
        if da == 0 and db > 1:
            relationship += "grand-"
        relationship += "mother " if da == 0 else "aunt "
        relationship += f"of {cow_b}"

with open("family.out", "w") as output_file:
    print(relationship, file=output_file)
