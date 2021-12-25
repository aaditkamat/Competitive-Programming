"""Day 2: Dive - https://adventofcode.com/2021/day/2"""

import argparse
import sys
from typing import List, Tuple

def part_1(commands: List[Tuple[str, int]]) -> int:
    final_horizontal_position, final_depth = 0, 0
    for command in commands:
        if command[0] == 'forward':
            final_horizontal_position += command[1]
        elif command[0] == 'down':
            final_depth += command[1]
        else:
            final_depth -= command[1]
    return final_horizontal_position * final_depth

def part_2(commands: List[Tuple[str, int]]) -> int:
    aim, final_horizontal_position, final_depth = 0, 0, 0
    for command in commands:
        if command[0] == 'forward':
            final_horizontal_position += command[1]
            final_depth += (aim * command[1])
        elif command[0] == 'down':
            aim += command[1]
        else:
            aim -= command[1]
    return final_horizontal_position * final_depth

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Solve Day 1 of AoC 2021")
    parser.add_argument(
        "input file", metavar="FILE", help="name of input file (day1.in)"
    )
    args: argparse.Namespace = parser.parse_args()
    file_name: str = sys.argv[1]
    with open(file_name) as f:
        lines = f.read().split('\n')
        commands: List[Tuple[str, int]] = []
        for line in lines:
            tokens = line.split(' ')
            commands.append((tokens[0], int(tokens[1])))
        print(f"Part 1: {part_1(commands)}")
        print(f"Part 2: {part_2(commands)}")
