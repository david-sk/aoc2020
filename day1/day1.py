#
# https://adventofcode.com/2020/day/1
#

from typing import List


def get_sorted_report() -> List[int]:
    with open('day1.input.txt') as f:
        report = [int(line) for line in f.readlines() if line]
        report.sort()
        return report


def day1_part1(report: List[int]) -> int:
    SUM_TARGET = 2020
    for i, entry in enumerate(report[:-1]):
        for other_entry in report[i + 1:]:
            sum_value = entry + other_entry
            if sum_value > SUM_TARGET:
                break
            if sum_value == SUM_TARGET:
                return entry * other_entry
    return -1


def day1_part2(report: List[int]) -> int:
    SUM_TARGET = 2020
    for i, entry in enumerate(report[:-2]):
        for j, second_entry in enumerate(report[i + 1:]):
            first_two_entries_sum = entry + second_entry
            if first_two_entries_sum > SUM_TARGET:
                break
            for third_entry in report[j + 1:]:
                sum_value = first_two_entries_sum + third_entry
                if sum_value > SUM_TARGET:
                    break
                if sum_value == SUM_TARGET:
                    return entry * second_entry * third_entry
    return -1


if __name__ == '__main__':
    report = get_sorted_report()
    print('Day1, part1 answer:', day1_part1(report))
    print('Day1, part2 answer:', day1_part2(report))
