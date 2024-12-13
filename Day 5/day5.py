from collections import defaultdict


class Day5_Part1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rules = defaultdict(list)
        self.update_orders = []
        self._parse_file()

    def _parse_file(self):
        second_section = False
        with open(self.filepath) as file:
            for line in file:
                if line == "\n":
                    second_section = True
                elif second_section:
                    self.update_orders.append(line.strip().split(","))
                else:
                    values = line.strip().split("|")
                    self.rules[values[0]].append(values[1])

    def get_middle_number_total_from_correct_update_orders(self):
        total = 0
        for update_order in self.update_orders:
            add_total = True
            discovered = set()
            for page1 in update_order:
                if page1 in self.rules.keys():
                    for page2 in self.rules[page1]:
                        if page2 in discovered:
                            add_total = False
                            break
                discovered.add(page1)
            if add_total:
                total += int(update_order[len(update_order) // 2])
        return total



if __name__ == "__main__":
    filepath = "./input.txt"
    day5_part1 = Day5_Part1(filepath)
    print(f"Part 1: {day5_part1.get_middle_number_total_from_correct_update_orders()}")
