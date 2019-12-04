def part1():
    first_wire_moves = input().split(',')
    second_wire_moves = input().split(',')
    curr = (0, 0)
    points = set()
    for move in moves1:
        distance = int(move[1:])
        vector = mapping[move[0]]
        for _ in range(distance):
            curr = tuple(vector[i] + curr[i] for i in range(len(vector)))
            points.add(curr)
    intersections = []
    curr = (0, 0)
    steps = 0
    for move in moves2:
        distance = int(move[1:])
        vector = mapping[move[0]]
        for _ in range(distance):
            steps += 1
            curr = tuple(vector[i] + curr[i] for i in range(len(vector)))
            if curr in points:
                intersections.append(curr)
    return min([x + y for (x, y) in intersections])

def part2():
    first_wire_moves = input().split(',')
    second_wire_moves = input().split(',')
    curr = (0, 0)
    steps = 0
    points = {}
    for move in moves1:
        distance = int(move[1:])
        vector = mapping[move[0]]
        for _ in range(distance):
            steps += 1
            curr = tuple(vector[i] + curr[i]for i in range(len(vector)))
            points[curr] = steps
    intersection_steps = []
    curr = (0, 0)
    steps = 0
    for move in moves2:
        distance = int(move[1:])
        vector = mapping[move[0]]
        for _ in range(distance):
            steps += 1
            curr = tuple(vector[i] + curr[i] for i in range(len(vector)))
            if curr in points:
                intersection_steps.append(points[curr] + steps)
    return min(intersection_steps)

mapping = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

print(part1())
print(part2())
