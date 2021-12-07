import math
fish = [int(timer.strip()) for timer in open('inputs/day6.txt').readline().split(',')]
def growth(fish, ndays):
    for _ in range(ndays):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)

print(growth(fish, 80)) # part 1



def reproductions_single(days_left, timer):
    return ((days_left - timer - 1) // 7) + 1
