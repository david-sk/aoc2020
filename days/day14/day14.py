#
# https://adventofcode.com/2020/day/14
#

from typing import List
from os import path
from itertools import combinations


def get_program() -> List[str]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [line.strip() for line in f.readlines() if line]


def day14_part1(program: List[str]) -> int:
    NUM_BITS = 36
    mask, mem = 'X' * NUM_BITS, {}
    for line in program:
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')[::-1]
        else:
            address, value = (
                int(str_value) for str_value in line.replace('mem[', '').split('] = ')
            )
            str_bin_value = bin(value).replace('0b', '')
            str_bin_value = (('0' * (NUM_BITS - len(str_bin_value))) + str_bin_value)[::-1]
            for i, c in enumerate(mask):
                if c != 'X' and str_bin_value[i] != c:
                    value += (1 if c == '1' else -1) * (2 ** i)
            mem[address] = value
    return sum(mem.values())


def day14_part2(program: List[str]) -> int:
    NUM_BITS = 36
    mask, mem = 'X' * NUM_BITS, {}
    for line in program:
        if line.startswith('mask'):
            mask = line.replace('mask = ', '')[::-1]
        else:
            address, value = (
                int(str_value) for str_value in line.replace('mem[', '').split('] = ')
            )
            str_bin_address = bin(address).replace('0b', '')
            str_bin_address = (('0' * (NUM_BITS - len(str_bin_address))) + str_bin_address)[::-1]
            x_indexes = [i for i, c in enumerate(mask) if c == 'X']
            first_address = sum(
                2 ** i
                for i, c in enumerate(mask)
                if c != 'X' and (c == '1' or str_bin_address[i] == '1')
            )
            mem[first_address] = value
            for num_indexes in range(1, len(x_indexes) + 1):
                for combination in combinations(x_indexes, r=num_indexes):
                    mem[first_address + sum(2 ** x_index for x_index in combination)] = value
    return sum(mem.values())


def main() -> None:
    program = get_program()
    print('Day13, part1 answer:', day14_part1(program))
    print('Day13, part2 answer:', day14_part2(program))
