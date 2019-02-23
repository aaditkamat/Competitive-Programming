def solution(num):
    first_sum = sum([pow(i, 2) for i in range(1, num + 1)])
    second_sum = pow(sum([i for i in range(1, num + 1)]), 2)
    return second_sum - first_sum

print(solution(100))