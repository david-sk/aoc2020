#
# https://adventofcode.com/2020/day/4
#

from typing import List, Dict, Optional
import re


PASSPORT_MANDATORY_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def get_passports() -> List[str]:
    with open('day4.input.txt') as f:
        return [line.strip() for line in f.readlines() if line]


def day4_part1(passports: List[str]) -> int:
    num_valid_passports = 0
    current_passport_fields: List[str] = []
    if passports[-1]:
        passports.append('')
    for line in passports:
        if not line:
            if len(current_passport_fields) > 0 and all(
                field in current_passport_fields for field in PASSPORT_MANDATORY_FIELDS
            ):
                num_valid_passports += 1
            current_passport_fields = []
        else:
            for key_value in line.split(' '):
                key, _ = key_value.split(':')
                current_passport_fields.append(key)
    return num_valid_passports


def day4_part2(passports: List[str]) -> int:
    color_pattern = re.compile('^#[a-f0-9]{6}$')

    def check_field(key: str, field_value: Optional[str]) -> bool:
        if field_value:
            if key == 'byr':
                return field_value.isdigit() and 1920 <= int(field_value) <= 2002
            if key == 'iyr':
                return field_value.isdigit() and 2010 <= int(field_value) <= 2020
            if key == 'eyr':
                return field_value.isdigit() and 2020 <= int(field_value) <= 2030
            if key == 'hgt':
                if 'cm' in field_value:
                    height = field_value.replace('cm', '')
                    return height.isdigit() and 150 <= int(height) <= 193
                if 'in' in field_value:
                    height = field_value.replace('in', '')
                    return height.isdigit() and 59 <= int(height) <= 76
            if key == 'hcl':
                return bool(color_pattern.match(field_value))
            if key == 'ecl':
                return field_value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
            if key == 'pid':
                return len(field_value) == 9 and field_value.isdigit()
        return False

    num_valid_passports = 0
    current_passport_fields: Dict[str, str] = {}
    if passports[-1]:
        passports.append('')
    for line in passports:
        if not line:
            if len(current_passport_fields) > 0 and all(
                check_field(field, current_passport_fields.get(field))
                for field in PASSPORT_MANDATORY_FIELDS
            ):
                num_valid_passports += 1
            current_passport_fields = {}
        else:
            for key_value in line.split(' '):
                key, value = key_value.split(':')
                current_passport_fields[key] = value
    return num_valid_passports


if __name__ == '__main__':
    passports = get_passports()
    print('Day4, part1 answer:', day4_part1(passports))
    print('Day4, part2 answer:', day4_part2(passports))
