with open('inputs/input_day2.txt', 'r') as file:
    commands = [line.strip() for line in file.readlines()]
    horizontal = 0
    vertical = 0
    for command in commands:
        command = command.split(" ")
        if command[0] == 'forward':
            horizontal += int(command[1])
        elif command[0] == 'up':
            vertical -= int(command[1])
        else:
            vertical += int(command[1])
print(horizontal * vertical) # part one

horizontal = 0
vertical = 0
aim = 0
for command in commands:
    command = command.split(" ")
    if command[0] == 'forward':
        horizontal += int(command[1])
        vertical += aim * int(command[1])
    elif command[0] == 'up':
        aim -= int(command[1])
    else:
        aim += int(command[1])
print(horizontal * vertical)
        