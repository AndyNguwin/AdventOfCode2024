from collections import defaultdict


class Day1_Part1:
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
    
class Day1_Part2:
    def __init__(self, filepath):
        self.filepath = filepath
        self.left_numbers = set()
        self.right_numbers = defaultdict(int)
        self._parse_file_to_get_dicts()
    
    def _parse_file_to_get_dicts(self):
        with open(self.filepath) as file:
            for line in file.readlines():
                splitted = line.split()
                self.left_numbers.add(int(splitted[0]))
                self.right_numbers[int(splitted[1])] += 1

    def calculate_similarity_score(self):
        score = 0
        for key in self.left_numbers:
            score += (key * self.right_numbers[key])
        return score

if __name__ == "__main__":
    # filepath = sys.argv[1]
    filepath = "./input.txt"
    day1_part1 = Day1_Part1(filepath)
    day1_part2 = Day1_Part2(filepath)
    print(f'Part 1: {day1_part1.calculate_total_distance()}')
    print(f'Part 2: {day1_part2.calculate_similarity_score()}')