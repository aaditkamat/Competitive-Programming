from math import floor, sqrt

def solution(num):
    start = 1
    i = 2
    while len(divisors(start)) * 2 <= num:
        start += i
        i += 1
    return num

def divisors(num):
    return [(i, num // i) for i in range(1, floor(sqrt(num)) + 1) if num % i == 0]

print(solution(500))