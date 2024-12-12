class Day4_Part1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.height = 0
        self.width = 0
        self.grid = []
        self._parse_file_for_grid()
    
    def _parse_file_for_grid(self):
        with open(self.filepath) as file:
            self.grid = file.readlines()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def _check_to_top_left(self, row, col):
        pass

    def _check_to_top_right(self, row, col):
        pass

    def _check_to_bottom_left(self, row, col):
        pass

    def _check_to_bottom_right(self, row, col):
        pass

    def _check_diagonals(self, row, col):
        pass

    def _check_to_left(self, row, col):
        if col < 3: return False
        elif (self.grid[row][col - 1] == "M" and
              self.grid[row][col - 2] == "A" and
              self.grid[row][col - 3] == "S"):
            return True
        return False

    def _check_to_right(self, row, col):
        if self.width - col < 4: return False
        elif (self.grid[row][col + 1] == "M" and
              self.grid[row][col + 2] == "A" and
              self.grid[row][col + 3] == "S"):
            return True
        return False

    def _check_to_top(self, row, col):
        if row < 3: return False
        elif (self.grid[row - 1][col] == "M" and
                self.grid[row - 2][col] == "A" and
                self.grid[row - 3][col] == "S"):
                return True
        return False

    def _check_to_bottom(self, row, col):
        if (self.height - row) < 4: return False
        elif (self.grid[row + 1][col] == "M" and
              self.grid[row + 2][col] == "A" and
              self.grid[row + 3][col] == "S"):
            return True
        return False

def _check_straights(self, row, col):
    if (self._check_to_left(row, col) or
        self._check_to_right(row, col) or
        self._check_to_top(row, col) or
        self._check_to_bottom(row, col)):
        return True
    return False

    def search_for_xmas(self):
        if self.height < 4 and self.width < 4: return 0
        pass
    

if __name__ == "__main__":
    filepath = "./input.txt"
    day4_part1 = Day4_Part1(filepath)
