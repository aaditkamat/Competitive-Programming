import argparse
import sys
from typing import List, Tuple, Set, Union


# Part 1
def two_sum(lst: List[int], total: int) -> Union[Tuple[int, int],  None] :
    container: Set[int] = set()
    for num in lst:
        if total - num in container:
            return (num, total - num)
        else:
            container.add(num)


# Part 2
def three_sum(lst: List[int], total: int) -> Union[Tuple[int, int, int], None]:
    container: Set[int] = set()
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
    args: argparse.Namespace = parser.parse_args()
    file_name: str = sys.argv[1]
    with open(file_name) as f:
        lst: List[int] = list(map(int, f.read().split()))
        result1: Union[Tuple[int, int], None] = two_sum(lst, 2020)
        if result1:
            num1, num2 = result1
            print(f"Part 1: The product of {num1} and {num2} is: {num1 * num2}")
        result2: Union[Tuple[int, int, int], None] = three_sum(lst, 2020)
        if result2:
            num1, num2, num3 = result2
            print(
                f"Part 2: The product of {num1}, {num2} and {num3} is: {num1 * num2 * num3}"
            )
