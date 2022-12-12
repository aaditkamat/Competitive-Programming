import heapq


def parse(file):
    lst, sub_lst = [], []
    for line in file:
        if line == '\n':
            lst.append(sub_lst)
            sub_lst = []
        else:
            sub_lst.append(int(line.strip('\n')))
    return lst


def part_1(lst):
    print(
        f'The total number of calories that the elf is carrying is: {max(sum(ele) for ele in lst)}'
    )


def part_2(lst):
    res, num_max = 0, 3
    sums_heap = [-1 * sum(ele) for ele in lst]
    heapq.heapify(sums_heap)
    for _ in range(num_max):
        res += -1 * heapq.heappop(sums_heap)
    print(f'The total number of calories that the elves are carrying is: {res}')


if __name__ == '__main__':
    path = './day1.in'
    with open(path) as file:
        lst = parse(file)
    part_1(lst)
    part_2(lst)
