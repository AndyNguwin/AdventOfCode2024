import re


class Day3_Part1:
    def __init__(self, filepath):
        self.filepath = filepath

    def _calculate_instruction_multiplied(self, instruction):
        total = 0
        all_muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instruction)
        for mul in all_muls:
            total += (int(mul[0]) * int(mul[1]))
        return total

    def total_multiplied(self):
        total = 0
        with open(self.filepath) as file:
            for line in file:
                total += self._calculate_instruction_multiplied(line)
        return total

if __name__ == "__main__":
    filepath = "./input.txt"
    day3_part1 = Day3_Part1(filepath)
    print(f"Part 1: {day3_part1.total_multiplied()}")