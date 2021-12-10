import numpy as np


lines = [line.strip() for line in open('inputs/day10.txt').readlines()]
error_values = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}
completion_values = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}
closing_values = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}
bracket_pairs = {']':'[', ')':'(', '>':'<', '}':'{'}
bracket_pairs_reversed = {'[':']', '(':')', '<':'>', '{':'}'}

def validate(line):
    stack = []
    offender = -1
    for char in line:
        if char in list(bracket_pairs.values()):
            stack.append(char)
        else:
            offender = char # will be a closing bracket
            if len(stack) > 0 and stack[len(stack) - 1] == bracket_pairs[offender]:
                stack.pop()
            else:
                return False, offender
    if len(stack) == 0:
        return True, ''
    else:
        return False, '' # the line was incomplete, so the offender is an empty string

def complete(line):
    stack = []
    offenders = []
    offender = ''
    for char in line:
        if char in list(bracket_pairs.values()):
            stack.insert(0, char)
            offenders.insert(0, bracket_pairs_reversed[char]) # assume this opening bracket has an issue (uncomplete)
        else:
            offender = char
            if len(stack) > 0 and stack[0] == bracket_pairs[offender]:
                stack.pop(0)
                offenders.pop(0) # issue resolved, current bracket no longer an offender 

    return offenders
total_error = 0
scores = []
for line in lines:
    result, offender = validate(line)
    if not result and offender != '':
        total_error += error_values[offender]
    if not result and offender == '':
        completion = complete(line)
        score = 0
        for char in completion:
            score *= 5
            score += completion_values[char]
        scores.append(score)

print(total_error)
print(int(np.median(scores)))
