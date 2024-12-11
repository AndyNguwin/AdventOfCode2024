class Day2_Part1:
    def __init__(self, filepath):
        self.filepath = filepath

    def _report_safe_check(self, report):
        if report[0] - report[1] > 0: 
            is_increasing = False
        else: 
            is_increasing = True
        
        for i in range(len(report) - 1):
            difference = report[i] - report[i+1]
            if difference == 0: return False
            if abs(difference) > 3: return False
            if is_increasing and difference > 0: return False
            if not is_increasing and difference < 0: return False
        return True
    
    def get_safe_reports_count(self):
        safe_count = 0
        with open(filepath) as file:
            for line in file:
                report = [int(x) for x in line.split()]
                if self._report_safe_check(report): safe_count += 1
        return safe_count

if __name__ == "__main__":
    filepath = "./input.txt"
    day2_part1 = Day2_Part1(filepath)
    print(f"Part 1: {day2_part1.get_safe_reports_count()} safe reports")