#
# https://adventofcode.com/2020/day/2
#

from typing import List


def get_password_list() -> List[str]:
    with open('day2.input.txt') as f:
        return [line for line in f.readlines() if line]


def day2_part1(password_list: List[str]) -> int:
    num_valid_passwords = 0
    for entry in password_list:
        left, right = entry.split(':')
        min_max, letter = left.split(' ')
        password = right.strip()
        min_letter, max_letter = [int(value) for value in min_max.split('-')]
        if min_letter <= password.count(letter) <= max_letter:
            num_valid_passwords += 1
    return num_valid_passwords


def day2_part2(password_list: List[str]) -> int:
    num_valid_passwords = 0
    for entry in password_list:
        left, right = entry.split(':')
        indexes, letter = left.split(' ')
        password = right.strip()
        index_1, index_2 = [int(value) - 1 for value in indexes.split('-')]
        password_len = len(password)
        index_1_valid = index_1 < password_len and password[index_1] == letter
        index_2_valid = index_2 < password_len and password[index_2] == letter
        if index_1_valid != index_2_valid:
            num_valid_passwords += 1
    return num_valid_passwords


if __name__ == '__main__':
    password_list = get_password_list()
    print('Day2, part1 answer:', day2_part1(password_list))
    print('Day2, part2 answer:', day2_part2(password_list))
