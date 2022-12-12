import pandas as pd
import string


def parse_part1(file):
    first_compartment, second_compartment = [], []
    for line in file:
        first_compartment.append(line[: len(line) // 2])
        second_compartment.append(line[len(line) // 2:])
    return pd.DataFrame({'first_compartment': first_compartment, 'second_compartment': second_compartment})


def parse_part2(file):
    lines = [line.strip('\n') for line in file]
    return pd.DataFrame(
        {
            'first_rucksack': lines[::3],
            'second_rucksack': lines[1::3],
            'third_rucksack': lines[2::3],
        }
    )


def part_1():
    path = './day3.in'

    with open(path) as file:
        df = parse_part1(file)
        first_compartment, second_compartment = df['first_compartment'], df['second_compartment']
        item_types = [
            set(first_item).intersection(set(second_item)).pop()
            for first_item, second_item in zip(
                first_compartment, second_compartment
            )
        ]
        df['item_type'] = pd.Series(item_types)
        df['priority'] = [string.ascii_letters.find(item) + 1 for item in df['item_type']]
        print(f'Sum of the priorities of the item types is: {df["priority"].sum()}')


def part_2():
    path = './day3.in'

    with open(path) as file:
        df = parse_part2(file)
        first_rucksack, second_rucksack, third_rucksack = df[
            'first_rucksack'], df['second_rucksack'], df['third_rucksack']
        badges = [
            set(first_item)
            .intersection(set(second_item))
            .intersection(set(third_item))
            .pop()
            for first_item, second_item, third_item in zip(
                first_rucksack, second_rucksack, third_rucksack
            )
        ]
        df['badges'] = pd.Series(badges)
        df['priority'] = [string.ascii_letters.find(badge) + 1 for badge in df['badges']]
        print(f'Sum of the priorities of the item types is: {df["priority"].sum()}')


if __name__ == '__main__':
    part_1()
    part_2()
