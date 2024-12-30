import fileinput

def up(grid, i, j):
    n = len(grid)
    if i < 3:
        return -1
    prod = 1
    for k in range(4):
        prod *= grid[i - k][j]
    return prod

def down(grid, i, j):
    n = len(grid)
    if i >= n - 3:
        return -1
    prod = 1
    for k in range(4):
        prod *= grid[i + k][j]
    return prod

def left(grid, i, j):
    n = len(grid[i])
    if j < 3:
        return -1
    prod = 1
    for k in range(4):
        prod *= grid[i][j - k]
    return prod

def right(grid, i, j):
    n = len(grid[i])
    if j >= n - 3:
        return -1
    prod = 1
    for k in range(4):
        prod *= grid[i][j + k]
    return prod

def diagonal(grid, i, j):
    n = len(grid)
    prod1, prod2, prod3, prod4 = 1, 1, 1, 1
    if up(grid, i, j) != -1 and left(grid, i, j) != -1:
        for k in range(4):
            prod1*= grid[i - k][j - k]
    if up(grid, i, j) != -1 and right(grid, i, j) != -1:
        for k in range(4):
            prod2*= grid[i - k][j + k]
    if down(grid, i, j) != -1 and left(grid, i, j) != -1:
        for k in range(4):
            prod3*= grid[i + k][j - k]
    if down(grid, i, j) != -1 and right(grid, i, j) != -1:
        for k in range(4):
            prod4*= grid[i + k][j + k]
    return max(prod1, prod2, prod3, prod4)

def solution(grid):
    lst = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            lst.append(max([up(grid, i, j), down(grid, i, j), left(grid, i, j), right(grid, i, j), diagonal(grid, i, j)]))
    return max(lst)

    
with open('Inputs/problem_11.in') as file:
    grid = []
    for line in file:
        grid.append([int(num) for num in line.split(' ')])
    print(solution(grid))
