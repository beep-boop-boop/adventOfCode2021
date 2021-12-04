file = open('inputs/day4.txt', 'r')
numbers = file.readline()
numbers = [int(num.strip()) for num in numbers.split(",")]
raw_boards = file.readlines()[1::]
boards = [[]]
for i in range(len(raw_boards)):
    if raw_boards[i] == '\n':
        boards.append([])
    else:
        boards[len(boards) - 1].append([[int(num), 0] for num in raw_boards[i].strip().split(" ") if num != ""]) #storing numbers as tuples, with 0 or 1 representing whether they are marked or not

def is_bingo(board):
    for row in board:
        if sum([num[1] for num in row]) == len(row):
            return True
    for col in range(len(board[0])):
        if sum(row[col][1] for row in board) == len(board):
            return True
    return False

def mark_number(num, board):
    for row in board:
        for i in range(len(row)):
            if row[i][0] == num:
                row[i][1] = 1
                return True
    return False

def score(board, number):
    summ = 0
    for row in board:
        for num in row:
            if num[1] == 0:
                summ += num[0]
    return summ * number

def play_bingo_first(numbers, boards):
    for num in numbers:
        for board in boards:
            if mark_number(num, board):
                if is_bingo(board):
                    return board, num

def play_bingo_last(numbers, boards):
    for num in numbers:
        for board in boards:
            if not is_bingo(board): # not marking boards which have already bingoed
                if mark_number(num, board):
                    if is_bingo(board):
                        last_board = board
                        last_num = num
    return last_board, last_num

first_board, first_num = play_bingo_first(numbers, boards)
print("part one:", score(first_board, first_num))

last_board, last_num = play_bingo_last(numbers, boards)
print("part two:", score(last_board, last_num))
