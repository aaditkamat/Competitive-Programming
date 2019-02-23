def gcd(x, y):
    arr = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            arr.append(i)
    return arr[-1]

def lcm(x, y):
    return (x * y) // gcd(x, y)

def solution(num):
    result = 2
    for i in range(3, num):
        result = lcm(result, i)
    return result

print(solution(20))