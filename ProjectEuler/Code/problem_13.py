
def solution(nums):
    total = sum(nums)
    return int(str(total)[:10])

with open('Inputs/problem_13.in') as file:
    nums = []
    for line in file:
        nums.append(int(line))
    print(solution(nums))
