with open('C:/Desktop/University-yr2/Advent of code 2021/day 1/input.txt', 'r') as file:
    numbers = file.readlines()
    numbers = [int(number.strip()) for number in numbers]
    groups = []
    count = 0
    for i in range(len(numbers) - 2):
        groups.append([])
        for d in range(i, i + 3):
            groups[i].append(numbers[d])
    groups = [sum(group) for group in groups]
    for i in range(len(groups) - 1):
        if groups[i + 1] > groups[i]:
            count += 1
print(count)