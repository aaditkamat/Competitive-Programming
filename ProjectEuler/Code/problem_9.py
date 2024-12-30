from math import pow
def are_triplet(i, j, k):
    return pow(i, 2) + pow(j, 2) == pow(k, 2)

def solution(num):
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if i + j + k == num and are_triplet(i, j, k):
                    return i * j * k
    return -1

print(solution(1000))