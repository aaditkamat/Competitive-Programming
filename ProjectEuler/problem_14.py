def collatz(num):
    length = 1
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        length += 1
    return length

def solution(num):
    max_length = 1
    value = 1
    for i in range(1, num):
        chain_length = collatz(i)
        if chain_length > max_length:
            max_length = chain_length
            value = i
    return value

print(solution(1000000))