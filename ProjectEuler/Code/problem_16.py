def solution(num):
    return sum([int(digit) for digit in str(pow(2, num))])

print(solution(1000))