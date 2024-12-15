class Day7_Part1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.calibration_total = 0
        self._calculate_calibration()
    
    def _check_for_add_or_mul_to_be_true(self, values, current, target):
        if len(values) == 0:
            return True if current == target else False
        current_val = values[0]
        add_to_current = current + current_val
        mul_to_current = current * current_val
        # print("Target: {target}")
        # print(f"Add {current_val} to {current}: {add_to_current}")
        # print(f"Muk {current_val} to {current}: {mul_to_current}")
        if (self._check_for_add_or_mul_to_be_true(values[1:], add_to_current, target) or
            self._check_for_add_or_mul_to_be_true(values[1:], mul_to_current, target)):
            return True
        return False
    
    def _calculate_calibration(self):
        with open(self.filepath) as file:
            self.calibration_total = 0
            for equation in file:
                equation = equation.strip()
                equation_split = equation.split(": ")
                target = int(equation_split[0])
                values = [int(value) for value in equation_split[1].split()]
                if (self._check_for_add_or_mul_to_be_true(values, 0, target)):
                    self.calibration_total += target
    
    def get_calibration_total(self):
        return self.calibration_total

if __name__ == "__main__":
    filepath = "./input.txt"
    day7_part1 = Day7_Part1(filepath)
    print(f"Part 1: {day7_part1.get_calibration_total()}")
