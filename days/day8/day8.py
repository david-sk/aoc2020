#
# https://adventofcode.com/2020/day/8
#

from typing import List, Set


def get_instructions() -> List[str]:
    with open('day8.input.txt') as f:
        return [line.strip() for line in f.readlines() if line]


def day8_part1(instructions: List[str]) -> int:
    run_indexes: Set[int] = set()

    def run_instruction(i: int) -> int:
        if i in run_indexes:
            return 0
        run_indexes.add(i)
        opcode, argument = instructions[i].split(' ')
        if opcode == 'acc':
            return int(argument) + run_instruction(i + 1)
        if opcode == 'jmp':
            return run_instruction(i + int(argument))
        return run_instruction(i + 1)

    return run_instruction(0)


def day8_part2(instructions: List[str]) -> int:
    last_index = len(instructions) - 1
    non_reachable_indexes: Set[int] = set()

    def find_non_reachable_indexes(target_index: int) -> None:
        is_reachable = False
        for i, instruction in enumerate(instructions):
            opcode, argument = instructions[i].split(' ')
            if (i + int(argument) if opcode == 'jmp' else i + 1) == target_index:
                find_non_reachable_indexes(i)
                is_reachable = True
        if not is_reachable:
            non_reachable_indexes.add(target_index)

    find_non_reachable_indexes(last_index)

    def run_instruction(i: int, may_fix: bool) -> int:
        if i > last_index:
            return 0
        opcode, argument = instructions[i].split(' ')
        if may_fix:
            if opcode == 'jmp' and i + 1 in non_reachable_indexes:
                opcode = 'nop'
                may_fix = False
            elif opcode == 'nop' and i + int(argument) in non_reachable_indexes:
                opcode = 'jmp'
                may_fix = False
        if opcode == 'acc':
            return int(argument) + run_instruction(i + 1, may_fix)
        if opcode == 'jmp':
            return run_instruction(i + int(argument), may_fix)
        return run_instruction(i + 1, may_fix)

    return run_instruction(0, True)


if __name__ == '__main__':
    instructions = get_instructions()
    print('Day8, part1 answer:', day8_part1(instructions))
    print('Day8, part2 answer:', day8_part2(instructions))
