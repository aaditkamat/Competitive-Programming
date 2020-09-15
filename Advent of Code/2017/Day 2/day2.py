def solve(spreadsheet, func):
    result = 0
    for row in spreadsheet[: -1]:
        result += func(row)
    return result

def func1(row):
    return max(row) - min(row)

def func2(row):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[j] % row [i] == 0:
                return row[j] // row[i]
            if row[i] % row[j] == 0:
                return row[i] // row[j]

if __name__ == '__main__':
    solve_part1 = lambda spreadsheet: solve(spreadsheet, func1)
    solve_part2 = lambda captcha: solve(captcha, func2)
    with open('day2.in') as file:
        # convert input to numeric_spreadsheet
        spreadsheet = [[int(num) for num in row.split('\t') if not num == ''] for row in file.read().split('\n')]
        print(f'Solution to Part 1: {solve_part1(spreadsheet)}')
        print(f'Solution to Part 2: {solve_part2(spreadsheet)}')