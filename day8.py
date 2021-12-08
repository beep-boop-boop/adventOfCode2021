screens = [line.strip().split(" | ") for line in open('inputs/day8.txt', 'r').readlines()]

inputs = [screen[0].split(" ") for screen in screens]
outputs = [screen[1].split(" ") for screen in screens]

part_1 = 0
# since 1, 4, 7 and 8 each require different numbers of digits, we can simply look for 
# output patterns of needed lengths: 2, 4, 3 and 7 respectfully

for output in outputs:
    for digit in output:
        if len(digit) in [2, 4, 3, 7]:
            part_1 += 1

print(part_1)
total = 0
for i, o in zip(inputs, outputs):
    mapping = {}
    # see part one ------------------------------
    one = [num for num in i if len(num) == 2][0]
    mapping["".join(sorted(one))] = 1
    seven = [num for num in i if len(num) == 3][0]
    mapping["".join(sorted(seven))] = 7
    eight = [num for num in i if len(num) == 7][0]
    zero = [num for num in i if len(num) == 6][0]
    mapping["".join(sorted(eight))] = 8
    four = [num for num in i if len(num) == 4][0]
    mapping["".join(sorted(four))] = 4
    #--------------------------------------------
    nine_or_six_or_zero = [num for num in i if len(num) == 6]
    for candidate in nine_or_six_or_zero:
        if sum([1 if char not in candidate else 0 for char in one]) == 1: # 9 and 0 both contain the entirety of 1, while 6 does not
            six = candidate
            mapping["".join(sorted(six))] = 6
    nine_or_zero = [item for item in nine_or_six_or_zero if item != six]
    nine, zero = '', ''
    for candidate in nine_or_zero:
        if sum([1 if char in candidate else 0 for char in four]) == 4: # 9 contains the entirety of 4, while 0 does not
            nine = candidate
        else:
            zero = candidate
    mapping["".join(sorted(zero))] = 0
    mapping["".join(sorted(nine))] = 9
    five_or_two_or_three = [num for num in i if len(num) == 5]
    five, two, three = '','',''
    for candidate in five_or_two_or_three:
        if sum([1 if char not in candidate else 0 for char in four]) == 2: # two differs from four by 2 digits, while 5 and 3 differ by one
            two = candidate
        elif sum([1 if char in candidate else 0 for char in seven]) == 3: # three contains the entirety of 7, while 2 and 5 do not
            three = candidate
        else:
            five = candidate
    mapping["".join(sorted(five))] = 5
    mapping["".join(sorted(three))] = 3
    mapping["".join(sorted(two))] = 2
    out_num = int("".join([str(mapping["".join(sorted(num))]) for num in o]))
    total += out_num

print(total)

    