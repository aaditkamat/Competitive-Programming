def prod(string):
    start = 1
    for char in string:
        start *= int(char)
    return start

def solution(string):
    lst = []
    for i in range(len(string) - 13):
        lst.append(prod(string[i: i + 13]))
    return max(lst)


with open('problem_8.txt') as file:
    string = ''
    for line in file:
        string += line.strip()
    print(solution(string))
