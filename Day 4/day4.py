class Day4_Part1:
    def __init__(self, filepath):
        self.filepath = filepath
        self.height = 0
        self.width = 0
        self.crossword = self._parse_file_for_crossword(filepath)
    
    def _parse_file_for_crossword(self)
        with open(self.filepath) as file:
            self.crossword = file.readlines()
        self.height = len(self.crossword)
        self.width = len(self.crossword[0])
    
    def _check_diagonals(self, row, col):
        pass

    def _check_to_top_left(self, row, col):
        pass

    def _check_to_top_right(self, row, col):
        pass

    def _check_to_bottom_left(self, row, col):
        pass

    def _check_to_bottom_right(self, row, col):
        pass

    def _check_staights(self, row, col):
        pass

    def _check_to_left(self, row, col):
        pass

    def _check_to_right(self, row, col):
        pass

    def _check_to_top(self, row, col):
        pass

    def _check_to_bottom(self, row, col)

    def search_for_xmas(self):
        pass
    

if __name__ == "__main__":
    filepath = "./input.txt"
    day4_part1 = Day4_Part1(filepath)
