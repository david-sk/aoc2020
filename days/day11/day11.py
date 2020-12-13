#
# https://adventofcode.com/2020/day/11
#

from typing import List, Tuple
from os import path


def get_seats() -> List[List[str]]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [[c for c in line.strip()] for line in f.readlines() if line]


def day11_part1(initial_seats: List[List[str]]) -> int:
    # copy to not mess with day11_part2, but otherwise not needed
    seats = [seat_row.copy() for seat_row in initial_seats]

    num_rows, num_cols = len(seats), len(seats[0])

    while True:
        changes: List[Tuple[int, int]] = []

        for i in range(num_rows):
            for j, seat in enumerate(seats[i]):
                if seat == '.':
                    continue
                num_occupied_adjacent = sum(
                    seats[i_adj][j_adj] == '#'
                    for i_adj in range(max(0, i - 1), min(num_rows, i + 2))
                    for j_adj in range(max(0, j - 1), min(num_cols, j + 2))
                    if (i_adj, j_adj) != (i, j)
                )
                if (seat == 'L' and num_occupied_adjacent == 0) or (
                    seat == '#' and num_occupied_adjacent >= 4
                ):
                    changes.append((i, j))

        if len(changes) == 0:
            break

        for i, j in changes:
            seats[i][j] = '#' if seats[i][j] == 'L' else 'L'

    return sum(seat_row.count('#') for seat_row in seats)


def day11_part2(initial_seats: List[List[str]]) -> int:
    seats = [seat_row.copy() for seat_row in initial_seats]

    num_rows, num_cols = len(seats), len(seats[0])

    while True:
        changes: List[Tuple[int, int]] = []

        for i in range(num_rows):
            for j, seat in enumerate(seats[i]):
                if seat == '.':
                    continue
                num_occupied_visible = 0
                for row_range in (range(i + 1, num_rows), range(i - 1, -1, -1)):
                    for i_vis in row_range:
                        if seats[i_vis][j] != '.':
                            num_occupied_visible += seats[i_vis][j] == '#'
                            break
                for col_range in (range(j + 1, num_cols), range(j - 1, -1, -1)):
                    for j_vis in col_range:
                        if seats[i][j_vis] != '.':
                            num_occupied_visible += seats[i][j_vis] == '#'
                            break
                for i_vis_update_value, j_vis_update_value in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                    i_vis, j_vis = i_vis_update_value, j_vis_update_value
                    while 0 <= i + i_vis < num_rows and 0 <= j + j_vis < num_cols:
                        if seats[i + i_vis][j + j_vis] != '.':
                            num_occupied_visible += seats[i + i_vis][j + j_vis] == '#'
                            break
                        i_vis, j_vis = i_vis + i_vis_update_value, j_vis + j_vis_update_value
                if (seat == 'L' and num_occupied_visible == 0) or (
                    seat == '#' and num_occupied_visible >= 5
                ):
                    changes.append((i, j))

        if len(changes) == 0:
            break

        for i, j in changes:
            seats[i][j] = '#' if seats[i][j] == 'L' else 'L'

    return sum(seat_row.count('#') for seat_row in seats)


def main() -> None:
    seats = get_seats()
    print('Day11, part1 answer:', day11_part1(seats))
    print('Day11, part2 answer:', day11_part2(seats))
