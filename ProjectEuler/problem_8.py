import fileinput

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

print("Enter a string: ")
string = ''
for line in fileinput.input():
    string += line.strip()
print(solution(string.strip()))