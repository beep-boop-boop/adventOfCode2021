from collections import Counter
file = open('inputs/day14.txt').readlines()
template = {}
rules = {}
for line in file:
    if '->' not in line and line != '\n':
        template_str = line.strip()
    elif line != '\n':
        line = line.strip().split(" -> ")
        rules[line[0]] = line[1]

def to_pairs(template_str):
    template = {}
    pointer = 0
    while pointer < len(template_str) - 1:
        if template_str[pointer : pointer + 2] not in template:
            template[template_str[pointer : pointer + 2]] = 1
        else:
            template[template_str[pointer : pointer + 2]] += 1
        pointer += 1
    return template
template = to_pairs(template_str)

def step(temp, rules):
    temp_new = {}
    for item in temp:
        if item in rules:
            if item[0] + rules[item] in temp_new:
                temp_new[item[0] + rules[item]] += temp[item]
            else:
                temp_new[item[0] + rules[item]] = temp[item]
            if rules[item] + item[1] in temp_new:
                temp_new[rules[item] + item[1]] += temp[item]
            else:
                temp_new[rules[item] + item[1]] = temp[item]
    return temp_new

def count_diff(template):
    letters = set(list("".join(list(template.keys()))))
    counts = {}
    for letter in letters:
        counts[letter] = sum([template[pair] * pair.count(letter) for pair in template])//2 + \
            (1 if letter in [template_str[0], template_str[len(template_str) - 1]] else 0)
    return max(counts.values()) - min(counts.values())

def solve(template, rules, iterations):
    for _ in range(iterations):
        template = step(template, rules)
    return count_diff(template)


print(solve(template, rules, 10))
print(solve(template, rules, 40))

