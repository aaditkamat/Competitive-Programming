import fileinput

def solution():
    return str(sum([int(num) for num in fileinput.input()]))[0: 10]

print(solution())
