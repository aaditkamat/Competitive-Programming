def solution(num):
    i = 1
    j = 2
    result = 0
    while j <= num:
        if i % 2 == 0:
            result += i
        if j % 2 == 0:
            result += j
        i += j
        j += i
    return result

print(solution(4000000))