#
# https://adventofcode.com/2020/day/12
#

from typing import List, Tuple
from os import path


def get_instructions_lines() -> List[str]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [line.strip() for line in f.readlines() if line]


def day12_part1(instructions: List[Tuple[str, int]]) -> int:
    directions = ('east', 'south', 'west', 'north')
    direction_index = 0
    north, east = 0, 0

    for action, value in instructions:
        if action in ('N', 'S'):
            north += value * (1 if action == 'N' else -1)
        elif action in ('E', 'W'):
            east += value * (1 if action == 'E' else -1)
        elif action == 'F':
            if directions[direction_index] in ('east', 'west'):
                east += value * (1 if directions[direction_index] == 'east' else -1)
            elif directions[direction_index] in ('north', 'south'):
                north += value * (1 if directions[direction_index] == 'north' else -1)
        elif action in ('L', 'R'):
            direction_index = (direction_index + value * (1 if action == 'R' else -1) // 90) % 4

    return abs(north) + abs(east)


def day12_part2(instructions: List[Tuple[str, int]]) -> int:
    waypoint = (10, 1)
    north, east = 0, 0

    for action, value in instructions:
        if action in ('N', 'S'):
            waypoint = (waypoint[0], waypoint[1] + value * (1 if action == 'N' else -1))
        elif action in ('E', 'W'):
            waypoint = (waypoint[0] + value * (1 if action == 'E' else -1), waypoint[1])
        elif action == 'F':
            north, east = north + waypoint[0] * value, east + waypoint[1] * value
        elif action == 'L':
            for _ in range(value // 90):
                waypoint = (-waypoint[1], waypoint[0])
        elif action == 'R':
            for _ in range(value // 90):
                waypoint = (waypoint[1], -waypoint[0])

    return abs(north) + abs(east)


def main() -> None:
    instructions_lines = get_instructions_lines()
    instructions = [
        (instructions_line[0], int(instructions_line[1:]))
        for instructions_line in instructions_lines
    ]
    print('Day12, part1 answer:', day12_part1(instructions))
    print('Day12, part2 answer:', day12_part2(instructions))
