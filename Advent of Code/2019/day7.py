def part1():
    lst = [int(x) for x in input()]
    mapping = {}
    grid = []
    for i in range(0, len(lst), 150):
        mapping[len([x for x in lst[i: i + 150] if x == 0])] = lst[i: i + 150]
    best = min(list(mapping.keys()))
    print(len([x for x in mapping[best] if x == 1]) * len([x for x in mapping[best] if x == 2]))



def part2():
    lst = [int(x) for x in input()]
    mapping = {}
    grid = []
    for i in range(0, len(lst), 150):
        grid.append(lst[i: i + 150])
    result = []
    flag = False
    for i in range(150):
        for j in range(len(grid)):
            if grid[j][i] != 2:
                flag = True
                result.append(grid[j][i])
                break
        if not flag:
            result.append(0)
    for i in range(6):
        for j in range(25):
            if result[25 * i + j] == 1:
                print("0", end='')
            else:
                print("1", end='')
        print()
