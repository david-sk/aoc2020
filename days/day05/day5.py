#
# https://adventofcode.com/2020/day/5
#

from typing import List
from os import path


def get_boarding_passes() -> List[str]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [line.strip() for line in f.readlines() if line]


def day5_part1(boarding_passes: List[str]) -> int:
    highest_seat_id = -1
    for boarding_passe in boarding_passes:
        lower_row, upper_row = 0, 127
        lower_col, upper_col = 0, 7
        for letter in boarding_passe:
            if letter == 'F':
                upper_row = (upper_row + lower_row) // 2
            elif letter == 'B':
                lower_row = (upper_row + lower_row) // 2
            elif letter == 'L':
                upper_col = (upper_col + lower_col) // 2
            elif letter == 'R':
                lower_col = (upper_col + lower_col) // 2
        highest_seat_id = max(highest_seat_id, upper_row * 8 + upper_col)
    return highest_seat_id


def day5_part2(boarding_passes: List[str]) -> int:
    seat_ids = []
    for boarding_passe in boarding_passes:
        lower_row, upper_row = 0, 127
        lower_col, upper_col = 0, 7
        for letter in boarding_passe:
            if letter == 'F':
                upper_row = (upper_row + lower_row) // 2
            elif letter == 'B':
                lower_row = (upper_row + lower_row) // 2
            elif letter == 'L':
                upper_col = (upper_col + lower_col) // 2
            elif letter == 'R':
                lower_col = (upper_col + lower_col) // 2
        seat_ids.append(upper_row * 8 + upper_col)

    seat_ids.sort()

    for i, seat_id in enumerate(seat_ids[1:], start=1):
        if seat_id - 1 != seat_ids[i - 1]:
            return seat_id - 1
    return -1


def main() -> None:
    boarding_passes = get_boarding_passes()
    print('Day5, part1 answer:', day5_part1(boarding_passes))
    print('Day5, part2 answer:', day5_part2(boarding_passes))
