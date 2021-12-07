crabs = [int(crab) for crab in open('inputs/day7.txt', 'r').readline().split(',')]

min_fuel = 1000000
for position in range(len(crabs)):
    min_attempt = sum([abs(crab - position) for crab in crabs])
    if min_attempt < min_fuel:
        min_fuel = min_attempt

print(min_fuel)

min_fuel_increasing = 100000000

for position in range(len(crabs)):
    """
    To find the fuel needed to move x steps, we need to find the sum of the first x numbers
    This is done using the formula for arithmetic progressions, where the sum of the first x numbers is (x * (x + 1)) / 2 
    """
    min_attempt = int(sum([(abs(crab - position) * ((abs(crab - position) + 1))) / 2 for crab in crabs])) 
    if min_attempt < min_fuel_increasing:
        min_fuel_increasing = min_attempt

print(min_fuel_increasing)