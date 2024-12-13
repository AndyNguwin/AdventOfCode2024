from collections import defaultdict


class Day5:
    def __init__(self, filepath):
        self.filepath = filepath
        self.rules = defaultdict(list)
        self.update_orders = []
        self.correct_orders = set()
        self.incorrect_orders = set()
        self._parse_file()
        self._categorize_update_orders()

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

    def _categorize_update_orders(self):
        for update_order in enumerate(self.update_orders):
            correct = True
            discovered = set()
            for page1 in update_order[1]:
                if page1 in self.rules.keys():
                    for page2 in self.rules[page1]:
                        if page2 in discovered:
                            correct = False
                            break
                discovered.add(page1)
            if correct:
                self.correct_orders.add(update_order[0])
            else:
                self.incorrect_orders.add(update_order[0])


    def get_middle_number_total_from_correct_update_orders(self):
        total = 0
        for i in self.correct_orders:
            correct_order = self.update_orders[i]
            total += int(correct_order[len(correct_order) // 2])
        return total

    def get_middle_number_total_from_incorrect_update_orders(self):
        total = 0
        for i in self.incorrect_orders:
            incorrect_order = self.update_orders[i]
            new_order = incorrect_order[:]
            for page1_i in range(len(new_order)):
                page1 = incorrect_order[page1_i]
                page1_new_i = page1_i
                if page1 in self.rules.keys():
                    for page2 in self.rules[page1]:
                        try:
                            page2_i = new_order.index(page2)
                            if page2_i < page1_new_i:
                                new_order.pop(page1_new_i)
                                new_order.insert(page2_i, page1)
                                page1_new_i = page2_i
                        except ValueError:
                            pass
            total += int(new_order[len(new_order) // 2])
        return total



if __name__ == "__main__":
    filepath = "./input.txt"
    day5 = Day5(filepath)
    print(f"Part 1: {day5.get_middle_number_total_from_correct_update_orders()}")
    print(f"Part 2: {day5.get_middle_number_total_from_incorrect_update_orders()}")
