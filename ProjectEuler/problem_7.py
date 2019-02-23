from math import floor, sqrt

def is_prime(num):
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(num):
    ctr = 0
    i = 2
    while (ctr <= num):
        if is_prime(i):
            ctr += 1
        if ctr == num:
            break
        i += 1
    return i


print(solution(10001))