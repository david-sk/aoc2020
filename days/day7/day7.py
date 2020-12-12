#
# https://adventofcode.com/2020/day/7
#

from typing import List, Dict, Tuple, Set
from os import path


Rules = Dict[str, List[Tuple[str, int]]]


def get_rules() -> Rules:
    def get_rule_lines() -> List[str]:
        with open(path.join(path.dirname(__file__), 'input.txt')) as f:
            return [line.strip() for line in f.readlines() if line]

    rules: Rules = {}
    for rule_line in get_rule_lines():
        bag, contained_bags = rule_line[:-1].split(' bags contain ')
        rules[bag] = []
        for contained_bag in contained_bags.split(', '):
            if contained_bag == 'no other bags':
                continue
            num_bags, name = contained_bag.split(' ', 1)
            rules[bag].append((name.replace(' bags', '').replace(' bag', ''), int(num_bags)))
    return rules


def day7_part1(rules: Rules) -> int:
    found_bags: Set[str] = set()

    def find_bags(wanted_bag: str) -> None:
        for outer_name in rules:
            if outer_name in found_bags:
                continue
            if any(name == wanted_bag for name, _ in rules[outer_name]):
                found_bags.add(outer_name)
                find_bags(outer_name)

    find_bags('shiny gold')
    return len(found_bags)


def day7_part2(rules: Rules) -> int:
    found_amounts: Dict[str, int] = {}

    def find_amount(outer_name: str) -> int:
        if outer_name not in found_amounts:
            found_amounts[outer_name] = sum(
                num_bags * (1 + find_amount(name)) for name, num_bags in rules[outer_name]
            )
        return found_amounts[outer_name]

    return find_amount('shiny gold')


def main() -> None:
    rules = get_rules()
    print('Day7, part1 answer:', day7_part1(rules))
    print('Day7, part2 answer:', day7_part2(rules))
