#
# https://adventofcode.com/2020/day/3
#

from typing import List


def get_locations() -> List[str]:
    with open('day3.input.txt') as f:
        return [line.strip() for line in f.readlines() if line]


def day3_part1(locations: List[str]) -> int:
    num_trees = 0
    num_cells = len(locations[0])  # assume all rows with same num cells
    i = 0
    for row in locations:
        num_trees += row[i % num_cells] == '#'
        i += 3
    return num_trees


def day3_part2(locations: List[str]) -> int:
    result = 1
    num_cells = len(locations[0])  # assume all rows with same num cells
    for increment, step in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        num_trees = 0
        i = 0
        for row in locations[::step]:
            num_trees += row[i % num_cells] == '#'
            i += increment
        result *= num_trees
    return result


if __name__ == '__main__':
    password_list = get_locations()
    print('Day3, part1 answer:', day3_part1(password_list))
    print('Day3, part2 answer:', day3_part2(password_list))
