#
# https://adventofcode.com/2020/day/6
#

from typing import List, Set, Optional
from os import path


def get_answers() -> List[str]:
    with open(path.join(path.dirname(__file__), 'input.txt')) as f:
        return [line.strip() for line in f.readlines() if line]


def day6_part1(answers: List[str]) -> int:
    total = 0
    group_answers = ''
    for answer in answers:
        if answer:
            group_answers += answer
        else:
            total += len(set(c for c in group_answers))
            group_answers = ''
    return total


def day6_part2(answers: List[str]) -> int:
    total = 0
    group_answers_set: Optional[Set[str]] = None
    for answer in answers:
        if answer:
            if group_answers_set is None:
                group_answers_set = set(c for c in answer)
            else:
                group_answers_set = group_answers_set.intersection(set(c for c in answer))
        elif group_answers_set is not None:
            total += len(group_answers_set)
            group_answers_set = None
    return total


def main() -> None:
    answers = get_answers()
    answers.append('')
    print('Day6, part1 answer:', day6_part1(answers))
    print('Day6, part2 answer:', day6_part2(answers))
