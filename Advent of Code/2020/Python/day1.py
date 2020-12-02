import argparse
import sys
from typing import Tuple

# Part 1
def two_sum(lst: list, total: int) -> Tuple[int, int]:
    container: set[int] = set()
    for num in lst:
        if total - num in container:
            return (num, total - num)
        else:
            container.add(num)


# Part 2
def three_sum(lst: list, total: int) -> Tuple[int, int, int]:
    container: set[int] = set()
    for num in lst:
        tup = two_sum(lst, total - num)
        if tup:
            return (num, tup[0], tup[1])
        else:
            container.add(num)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve day1 of AoC 2020")
    parser.add_argument(
        "input file", metavar="FILE", help="name of input file (day1.in)"
    )
    file_name: str = sys.argv[1]
    with open(file_name) as f:
        lst: list = list(map(int, f.read().split()))
        num1, num2 = two_sum(lst, 2020)
        print(f"Part 1: The product of {num1} and {num2} is: {num1 * num2}")
        num1, num2, num3 = three_sum(lst, 2020)
        print(
            f"Part 2: The product of {num1}, {num2} and {num3} is: {num1 * num2 * num3}"
        )
