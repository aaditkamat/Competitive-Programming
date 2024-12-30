from math import floor, sqrt

def solution(num):
    start = 1
    i = 2
    while len(get_divisors(start)) < num:
        start += i
        i += 1
    return start

def get_divisors(num):
    divisors = set()
    for i in range(1, floor(sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

print(solution(500))