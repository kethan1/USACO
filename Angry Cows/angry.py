with open("angry.in") as input_file:
    input_file.readline()
    hay_bales = {int(line) for line in input_file}

def blast(hay_bales, bale_shot, blast_radius = 1):
    exploded = {hay_bale for hay_bale in hay_bales if 0 < abs(hay_bale-bale_shot) <= blast_radius}
    for hay_bale_exploded in exploded.copy():
        exploded |= blast({hay_bale for hay_bale in hay_bales if hay_bale not in exploded and hay_bale != bale_shot}, hay_bale_exploded, blast_radius + 1)
    return exploded

with open("angry.out", "w") as output_file:
    print(max([len(blast(hay_bales, bale) | {bale}) for bale in hay_bales]), file = output_file)

# using threading or asyncio
