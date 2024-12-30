from math import sqrt, floor

def is_prime(num):
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(num):
    prime_factors = []
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            if is_prime(i):
                prime_factors.append(i)
            elif is_prime(num / i):
                prime_factors.append(num / i)
    return max(prime_factors)

print(solution(600851475143))