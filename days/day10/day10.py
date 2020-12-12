#
# https://adventofcode.com/2020/day/10
#

from typing import List
from os import path
from math import prod


def get_jolts() -> List[int]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [int(line.strip()) for line in f.readlines() if line]


def day10_part1(sorted_jolts: List[int]) -> int:
    # we assume there is a 1, 2 or 3 jolt in the list (there is :), else it's easy to check),
    # hence one_diff = 1 to begin with
    one_diff, three_diff = 1, 0
    for i, jolt in enumerate(sorted_jolts[:-1]):
        if sorted_jolts[i + 1] - jolt == 1:
            one_diff += 1
        elif sorted_jolts[i + 1] - jolt == 3:
            three_diff += 1
        else:
            break
    return one_diff * (three_diff + 1)  # three_diff + 1 for the device's built-in


def day10_part2(sorted_jolts: List[int]) -> int:
    # getting the longest arrangement possible
    longest_arrangement = [sorted_jolts[0]]
    for i, jolt in enumerate(sorted_jolts[:-1]):
        if sorted_jolts[i + 1] - jolt in (1, 3):
            longest_arrangement.append(sorted_jolts[i + 1])
        else:
            longest_arrangement.append(longest_arrangement[-1] + 3)
            break

    # split the longest arrangement into chunks of 1 jolt differences, e.g.: [[1, 2], [5, 6], ...]
    arrangement_chunks_indexes = [
        i + 1
        for i, jolt in enumerate(longest_arrangement[:-1])
        if longest_arrangement[i + 1] - jolt == 3
    ]
    arrangement_chunks = []
    previous_index = 0
    for arrangement_chunks_index in arrangement_chunks_indexes:
        arrangement_chunks.append(longest_arrangement[previous_index:arrangement_chunks_index])
        previous_index = arrangement_chunks_index
    arrangement_chunks.append(longest_arrangement[previous_index:])

    # using recursion to count arrangements while removing possible jolt from the arrangement input
    def count_arrangements_by_removing_jolts(arrangement: List[int], start: int) -> int:
        return 1 + sum(
            count_arrangements_by_removing_jolts(arrangement[:i] + arrangement[i + 1 :], i)
            for i, _ in enumerate(arrangement[start:-1], start=start)
            if 0 < arrangement[i + 1] - arrangement[i - 1] <= 3
        )

    # the solution is the product of each count of arrangements for each chunk
    # note that we add the outer left/right jolts on each chunk that can't be
    # removed which is expected by the `count_arrangements_by_removing_jolts` function
    return prod(
        count_arrangements_by_removing_jolts(
            [max(0, arrangement_chunk[0] - 3)] + arrangement_chunk + [arrangement_chunk[-1] + 3], 1
        )
        for arrangement_chunk in arrangement_chunks
    )


def main() -> None:
    jolts = get_jolts()
    jolts.sort()
    print('Day10, part1 answer:', day10_part1(jolts))
    print('Day10, part2 answer:', day10_part2(jolts))
