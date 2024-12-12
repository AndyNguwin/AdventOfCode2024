class Day4_Part1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.height = 0
        self.width = 0
        self.grid = []
        self.xmas_count = 0
        self._parse_file_for_grid()
        self._search_for_xmas()
    
    def _parse_file_for_grid(self):
        with open(self.filepath) as file:
            self.grid = file.readlines()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def _check_to_top_left(self, row, col):
        if (row < 3 or col < 3): return
        elif (self.grid[row - 1][col - 1] == "M" and
              self.grid[row - 2][col - 2] == "A" and
              self.grid[row - 3][col - 3] == "S"):
            self.xmas_count += 1


    def _check_to_top_right(self, row, col):
        if (row < 3 or self.width - col < 4): return
        elif (self.grid[row - 1][col + 1] == "M" and
              self.grid[row - 2][col + 2] == "A" and
              self.grid[row - 3][col + 3] == "S"):
            self.xmas_count += 1

    def _check_to_bottom_left(self, row, col):

        if (self.height - row < 4 or col < 3): return
        elif (self.grid[row + 1][col - 1] == "M" and
              self.grid[row + 2][col - 2] == "A" and
              self.grid[row + 3][col - 3] == "S"):
            self.xmas_count += 1

    def _check_to_bottom_right(self, row, col):
        if (self.height - row < 4 or self.width - col < 4): return
        elif (self.grid[row + 1][col + 1] == "M" and
              self.grid[row + 2][col + 2] == "A" and
              self.grid[row + 3][col + 3] == "S"):
            self.xmas_count += 1

    def _check_diagonals(self, row, col):
        self._check_to_top_left(row, col)
        self._check_to_top_right(row, col)
        self._check_to_bottom_left(row, col)
        self._check_to_bottom_right(row, col)

    def _check_to_left(self, row, col):
        if col < 3: return
        elif (self.grid[row][col - 1] == "M" and
              self.grid[row][col - 2] == "A" and
              self.grid[row][col - 3] == "S"):
            self.xmas_count += 1

    def _check_to_right(self, row, col):
        if self.width - col < 4: return
        elif (self.grid[row][col + 1] == "M" and
              self.grid[row][col + 2] == "A" and
              self.grid[row][col + 3] == "S"):
            self.xmas_count += 1

    def _check_to_top(self, row, col):
        if row < 3: return
        elif (self.grid[row - 1][col] == "M" and
              self.grid[row - 2][col] == "A" and
              self.grid[row - 3][col] == "S"):
            self.xmas_count += 1

    def _check_to_bottom(self, row, col):
        if (self.height - row) < 4: return
        elif (self.grid[row + 1][col] == "M" and
              self.grid[row + 2][col] == "A" and
              self.grid[row + 3][col] == "S"):
            self.xmas_count += 1

    def _check_straights(self, row, col):
        self._check_to_left(row, col)
        self._check_to_right(row, col)
        self._check_to_top(row, col)
        self._check_to_bottom(row, col)

    def _search_for_xmas(self):
        if self.height < 4 and self.width < 4: return 0
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == "X":
                    self._check_diagonals(row, col)
                    self._check_straights(row, col)

    def get_xmas_count(self):
        return self.xmas_count
    

if __name__ == "__main__":
    filepath = "./input.txt"
    day4_part1 = Day4_Part1(filepath)
    print(f"Day 1: {day4_part1.get_xmas_count()} instances of 'XMAS'")
