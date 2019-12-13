from math import atan2, sqrt, sin
from functools import cmp_to_key

def count_direct(first, points):
    angles = set()
    for second in points:
        if second != first:
            dx, dy = second[1] - first[1], second[0] - first[0]
            angles.add(atan2(dy, dx))
    return len(angles)

def get_quadrant(dx, dy):
    if dx <= 0 and dy >= 0:
        return 1
    if dx > 0 and dy > 0:
        return 2
    if dx < 0 and dy > 0:
        return 3
    return 4

def cmp(value1, value2):
    if value1[0] != value2[0]:
        return -1 if value1[0] < value2[0] else 1
    if value1[1] != value2[1]:
        return -1 if value1[1] > value2[1] else 1
    return 0

def get_best_value_and_position(points):
    mapping = {point: count_direct(point, points) for point in points}
    best_value = max(mapping.values())
    best_position = next((mapping[point] == best_value for point in points))
    return best_value, best_position

def part1():
    grid = [list(row) for row in file_input.split('\n')]
    size = len(grid)
    points = set(((y, x) for x in range(size) for y in range(size) if grid[x][y] == '#'))
    best_value, best_position = get_best_value_and_position(points)
    # Answer for Part 1
    print(best_value)
    return best_position, points

def part2(first, points):
    mapping = {}
    compare_values = set()
    for second in points:
        if second != first:
            dx, dy = second[1] - first[1], second[0] - first[0]
            r = sqrt(pow(dx, 2) + pow(dy, 2))
            quad = get_quadrant(dx, dy)
            angle = atan2(dy, dx)
            compare_value = (quad, angle)
            compare_values.add(compare_value)
            if compare_value not in mapping:
                mapping[compare_value] = [(r, second)]
            else:
                mapping[compare_value].append((r, second))
    compare_values = sorted(compare_values, key=cmp_to_key(cmp))
    for compare_value in mapping:
        mapping[compare_value] = sorted(mapping[compare_value], key=lambda x: x[0])
    ctr = 0
    flag = True
    while flag:
        index = 0
        for compare_value in compare_values:
            ctr += 1
            if ctr == 200:
                # Answer for Part 2
                print(mapping[compare_value][index][1])
                return

def solve(file_input):
    best_position, points = part1()
    lst = part2(best_position, points)  


with open('day10.in', mode='r') as file_obj:
    file_input = file_obj.read()
    solve(file_input)