#
# https://adventofcode.com/2020/day/13
#

from typing import List
from os import path


def get_bus_info() -> List[str]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [line.strip() for line in f.readlines() if line]


def day13_part1(earliest_time: int, bus_ids: List[int]) -> int:
    target_time = earliest_time
    while True:
        for bus_id in bus_ids:
            if bus_id > 0 and target_time % bus_id == 0:
                return bus_id * (target_time - earliest_time)
        target_time += 1


def day13_part2(bus_ids: List[int]) -> int:
    # Cheating to use wolframalpha? :P
    # TODO: use some multiple equation solver in python instead :)

    bus_ids_with_indexes = [(bus_id, i) for i, bus_id in enumerate(bus_ids) if bus_id > 0]

    equations = ''
    for i, (bus_id, index) in enumerate(bus_ids_with_indexes):
        equations += f'{bus_id} * {chr(97 + i)} - {index} = n ; '
    equations = equations.strip(' ;')

    print('\nDay 13, part 2\nYou get a set of equations:\n')
    print(equations)
    print('\nCopy them, and paste them into https://www.wolframalpha.com :)')
    print('It will show some solutions, with the last one being n = [number_A]m + [number_B]')
    print('[number_B] is the solution')
    print('you can check it with the check below this print in the code')

    target_time = 379786358533423
    if all((target_time + index) % bus_id == 0 for bus_id, index in bus_ids_with_indexes):
        return target_time
    return -1


def main() -> None:
    bus_info = get_bus_info()
    earliest_time, bus_ids = (
        int(bus_info[0]),
        [int(bus_id) if bus_id != 'x' else 0 for bus_id in bus_info[1].split(',')],
    )
    print('Day13, part1 answer:', day13_part1(earliest_time, bus_ids))
    print('Day13, part2 answer:', day13_part2(bus_ids))
