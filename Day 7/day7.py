class Day7:
    def __init__(self, filepath):
        self.filepath = filepath
        self.calibration_total = 0
        # self._calculate_calibration()
    
    def _check_for_add_or_mul_to_be_true(self, values, current, target):
        if len(values) == 0:
            return True if current == target else False
        # if current >= target: return False
        current_val = values[0]
        add_to_current = current + current_val
        mul_to_current = current * current_val

        if (self._check_for_add_or_mul_to_be_true(values[1:], add_to_current, target) or
            self._check_for_add_or_mul_to_be_true(values[1:], mul_to_current, target)):
            return True
        return False
    
    def _check_for_add_mul_concat_to_be_true(self, values, current, target):
        if len(values) == 0:
            return True if current == target else False
        # if current >= target: return False
        current_val = values[0]
        add_to_current = current + current_val
        mul_to_current = current * current_val
        concat_to_current = int(str(current) + str(current_val))
        if (self._check_for_add_mul_concat_to_be_true(values[1:], add_to_current, target) or
            self._check_for_add_mul_concat_to_be_true(values[1:], mul_to_current, target) or
            self._check_for_add_mul_concat_to_be_true(values[1:], concat_to_current, target)):
            return True
        return False
    
    def _calculate_calibration(self, part):
        with open(self.filepath) as file:
            self.calibration_total = 0
            for equation in file:
                equation = equation.strip()
                equation_split = equation.split(": ")
                target = int(equation_split[0])
                values = [int(value) for value in equation_split[1].split()]
                if part == 1:
                    if (self._check_for_add_or_mul_to_be_true(values[1:], values[0], target)):
                        self.calibration_total += target
                elif part == 2:
                    if (self._check_for_add_mul_concat_to_be_true(values[1:], values[0], target)):
                        self.calibration_total += target
    
    def get_calibration_total(self, part):
        self._calculate_calibration(part)
        return self.calibration_total
    

if __name__ == "__main__":
    filepath = "./input.txt"
    day7 = Day7(filepath)
    print(f"Part 1: {day7.get_calibration_total(1)}")
    print(f"Part 2: {day7.get_calibration_total(2)}")
