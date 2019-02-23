from math import floor, sqrt

def is_prime(num):
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(num):
    return sum([i for i in range(2, num) if is_prime(i)])


print(solution(2000000))