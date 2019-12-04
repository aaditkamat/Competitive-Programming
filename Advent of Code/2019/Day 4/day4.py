
check_adj = lambda num: any([num[i] == num[i - 1] for i in range(1, len(num))])

check_never_decrease = lambda num: all([num[i] >= num[i - 1] for i in range(1, len(num))])

def check_adj2(num):
    count = {}
    for char in num:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return any([num[i] == num[i - 1] and count[num[i]] == 2 for i in range(1, len(num))])

check2 = lambda num: check_never_decrease(num) and check_adj2(num)

check1 = lambda num: check_adj(num) and check_never_decrease(num)

part1 = lambda start, end: sum([check1(str(num)) for num in range(start, end + 1)])

part2 = lambda start, end: sum([check2(str(num)) for num in range(start, end + 1)])

start, end = [int(num) for num in input().split('-')]

print(part1(start, end))

print(part2(start, end))