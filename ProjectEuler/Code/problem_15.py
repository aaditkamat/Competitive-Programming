def combinations(n, r):
    arr = []
    for i in range(n + 1):
        arr.append([0 for j in range(r + 1)])

    for i in range(n + 1):
        arr[i][0] = 1

    for i in range(min(n + 1, r + 1)):
        arr[i][i] = 1

    for i in range(n + 1):
        for j in range(1, r + 1):
            if i > j:
                arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]
    return arr[n][r]

def solution(num):
    return combinations(num * 2, num)

print(solution(20))