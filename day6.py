from collections import Counter
from functools import cache
fish = [int(timer.strip()) for timer in open('inputs/day6.txt').readline().split(',')]
def fish_growth(fish, ndays):
    @cache
    def growth(timer, ndays):
        if ndays == 0:
            return 1
        else:
            if timer == 0:
                return growth(8, ndays - 1) + growth(6, ndays - 1)
            else:
                return growth(timer - 1, ndays - 1)
    fish_count = Counter(fish)
    total = 0
    for timer in fish_count:
        total += growth(timer, ndays) * fish_count[timer]
    return total

print(fish_growth(fish, 80))
print(fish_growth(fish, 256))