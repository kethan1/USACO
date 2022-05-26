import itertools

N = int(input())
blocks = [set(input()) for _ in range(4)]
words = [input() for _ in range(N)]

for word in words:
    if len(word) == 1:
        if word in blocks[0] | blocks[1] | blocks[2] | blocks[3]:
            print("YES")
        else:
            print("NO")
    elif len(word) == 2:
        if (
            (word[0] in blocks[0] | blocks[1] and word[1] in blocks[2] | blocks[3])
            or (word[0] in blocks[0] | blocks[2] and word[1] in blocks[1] | blocks[3])
            or (word[0] in blocks[0] | blocks[3] and word[1] in blocks[1] | blocks[2])
            or (word[1] in blocks[0] | blocks[1] and word[0] in blocks[2] | blocks[3])
            or (word[1] in blocks[0] | blocks[2] and word[0] in blocks[1] | blocks[3])
            or (word[1] in blocks[0] | blocks[3] and word[0] in blocks[1] | blocks[2])
        ):
            print("YES")
        else:
            print("NO")
    elif len(word) == 3:
        possible = False
        for block_nums in itertools.permutations([0, 1, 2, 3], 3):
            if (
                word[0] in blocks[block_nums[0]]
                and word[1] in blocks[block_nums[1]]
                and word[2] in blocks[block_nums[2]]
            ):
                print("YES")
                possible = True
                break
        if not possible:
            print("NO")
    elif len(word) == 4:
        possible = False
        for block_nums in itertools.permutations([0, 1, 2, 3], 4):
            if (
                word[0] in blocks[block_nums[0]]
                and word[1] in blocks[block_nums[1]]
                and word[2] in blocks[block_nums[2]]
                and word[3] in blocks[block_nums[3]]
            ):
                print("YES")
                possible = True
                break
        if not possible:
            print("NO")
