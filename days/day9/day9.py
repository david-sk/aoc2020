#
# https://adventofcode.com/2020/day/9
#

from typing import List


def get_numbers() -> List[int]:
    with open('day9.input.txt') as f:
        return [int(line.strip()) for line in f.readlines() if line]


def day9_part1(numbers: List[int]) -> int:
    PREAMBLE_LENGTH = 25
    for i, number in enumerate(numbers[PREAMBLE_LENGTH:], start=PREAMBLE_LENGTH):
        previous_numbers = numbers[i - PREAMBLE_LENGTH : i]
        if not any(
            previous_number + second_previous_number == number
            for j, previous_number in enumerate(previous_numbers[:-1])
            for second_previous_number in previous_numbers[j + 1 :]
        ):
            return number
    return -1


def day9_part2(numbers: List[int]) -> int:
    IVALID_NUMBER = 21806024
    for i, first_number in enumerate(numbers[:-1]):
        set_amount = first_number
        for j, next_number in enumerate(numbers[i + 1 :], start=i + 1):
            set_amount += next_number
            if set_amount == IVALID_NUMBER:
                numbers_set = numbers[i : j + 1]
                return min(numbers_set) + max(numbers_set)
            if set_amount > IVALID_NUMBER:
                break
    return -1


if __name__ == '__main__':
    numbers = get_numbers()
    print('Day9, part1 answer:', day9_part1(numbers))
    print('Day9, part2 answer:', day9_part2(numbers))
