import argparse
import sys
from functools import reduce
from typing import List, Tuple


def count_trees(grid: List[List[str]], slopes: List[Tuple[int, int]]) -> int:
    ctrs: List[int] = []
    for dx, dy in slopes:
        ctr: int = 0
        x, y = 0, 0
        while x < len(grid):
            if grid[x][y] == "#":
                ctr += 1
            x += dx
            y = (y + dy) % len(grid[0])
        ctrs.append(ctr)
    return reduce(lambda x, y: x * y, ctrs, 1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve day3 of AoC 2020")
    parser.add_argument(
        "input file", metavar="FILE", help="name of input file (day3.in)"
    )
    file_name: str = sys.argv[1]
    with open(file_name) as f:
        grid: List[List[str]] = [list(row) for row in f.read().split()]

        # Part 1
        slopes: List[Tuple[int, int]] = [(1, 3)]
        num_trees: int = count_trees(grid, [(1, 3)])
        print(f"The number of trees encountered: {num_trees}")

        # Part 2
        slopes: List[Tuple[int, int]] = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
        mult_result: int = count_trees(grid, slopes)
        print(f"Multiplication of the number of trees encountered: {mult_result}")
