import sys


class Day1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.list1 = []
        self.list2 = []
        self._parse_file_to_get_list()
    
    def _parse_file_to_get_list(self):
        with open(self.filepath) as file:
            for line in file.readlines():
                splitted = line.split()
                self.list1.append(int(splitted[0]))
                self.list2.append(int(splitted[1]))
        self.list1 = sorted(self.list1)
        self.list2 = sorted(self.list2)

    def calculate_total_distance(self):
        total = 0
        for i in range(len(self.list1)):
            total += abs(self.list1[i] - self.list2[i])
        return total

if __name__ == "__main__":
    filepath = sys.argv[1]
    day1 = Day1(filepath)
    print(day1.calculate_total_distance())