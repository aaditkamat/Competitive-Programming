"""Day 1: Sonar Sweep - https://adventofcode.com/2021/day/1"""

import argparse
import sys
from typing import List

# Count the number of times a depth measurement increases from the previous measurement
def part_1(measurements: List[int]) -> int:
    ctr = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            ctr += 1
    return ctr

# Count the number of times the sum of measurements in this sliding window increases
def part_2(measurements: List[int]) -> int:
    ctr = 0
    for i in range(3, len(measurements)):
        if sum(measurements[i - 2: i + 1]) > sum(measurements[i - 3: i]):
            ctr += 1
    return ctr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Solve Day 1 of AoC 2021")
    parser.add_argument(
        "input file", metavar="FILE", help="name of input file (day1.in)"
    )
    args: argparse.Namespace = parser.parse_args()
    file_name: str = sys.argv[1]
    with open(file_name) as f:
        measurements: List[int] = [int(num_str) for num_str in f.read().split()]
        print(f"Part 1: {part_1(measurements)}")
        print(f"Part 2: {part_2(measurements)}")
