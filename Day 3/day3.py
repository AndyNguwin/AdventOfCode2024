import re


class Day3_Part1:
    def __init__(self, filepath):
        self.filepath = filepath

    def _calculate_instruction_multiplied(self, line):
        total = 0
        all_muls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        for mul in all_muls:
            total += (int(mul[0]) * int(mul[1]))
        return total

    def total_multiplied(self):
        total = 0
        with open(self.filepath) as file:
            for line in file:
                total += self._calculate_instruction_multiplied(line)
        return total
    
class Day3_Part2:
    def __init__(self, filepath):
        self.filepath = filepath

    def _calculate_instruction_multiplied(self, line, do):
        do = do
        total = 0
        instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))", line)
        for instruction in instructions:
            if instruction[0] == "do()":
                do = True
            elif instruction[0] == "don't()":
                do = False
            elif do:
                total += (int(instruction[1]) * int(instruction[2]))
        return (total, do)

    def total_multiplied(self):
        do = True
        total = 0
        with open(self.filepath) as file:
            for line in file:
                result = self._calculate_instruction_multiplied(line, do)
                total += result[0]
                do = result[1]
        return total

if __name__ == "__main__":
    filepath = "./input.txt"
    day3_part1 = Day3_Part1(filepath)
    day3_part2 = Day3_Part2(filepath)
    print(f"Part 1: {day3_part1.total_multiplied()}")
    print(f"Part 2: {day3_part2.total_multiplied()}")