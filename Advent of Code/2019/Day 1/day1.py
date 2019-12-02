def getTotal(num):
    total = 0
    while True:
        num = num // 3 - 2
        if num < 0:
            break
        total += num
    return total

part1 = lambda lst: sum([num // 3 - 2 for num in lst])
part2 = lambda lst: sum([getTotal(num) for num in lst])
lst = []
while True:
    try:
        lst.append(int(input()))
    except EOFError:
        break
print(part1(lst))
print(part2(lst))

