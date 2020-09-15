def solve(captcha, step):
    result = 0
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i + step) % len(captcha)]:
            result += int(captcha[i])
    return result

if __name__ == '__main__':
    solve_part1 = lambda captcha: solve(captcha, 1)
    solve_part2 = lambda captcha: solve(captcha, len(captcha) // 2)
    with open('day1.in') as file:
        captcha = file.read()
        print(f'Solution to Part 1: {solve_part1(captcha)}')
        print(f'Solution to Part 2: {solve_part2(captcha)}')