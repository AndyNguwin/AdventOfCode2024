class Day2:
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
    
    def _report_dampener_check(self, report):
        for i in range(len(report)):
            report_copy = report[:]
            report_copy.pop(i)
            if self._report_safe_check(report_copy):
                return True
        return False
    
    def get_safe_reports_count(self):
        safe_count = 0
        dampener_safe_count = 0
        with open(filepath) as file:
            for line in file:
                report = [int(x) for x in line.split()]
                if self._report_safe_check(report): safe_count += 1
                elif self._report_dampener_check(report): dampener_safe_count += 1
        return (safe_count, dampener_safe_count)

if __name__ == "__main__":
    filepath = "./input.txt"
    day2 = Day2(filepath)
    safe_reports = day2.get_safe_reports_count()
    print(f"Part 1: {safe_reports[0]} safe reports")
    print(f"Part 2: {safe_reports[0] + safe_reports[1]} safe reports")