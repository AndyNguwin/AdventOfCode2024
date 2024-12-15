class Day9:
    def __init__(self, filepath):
        self.filepath = filepath
        self.disk_map = []
        self._convert_disk_map()
        self._fill_gaps()
    
    def _convert_disk_map(self):
        is_file = True
        # index = 0
        id = 0
        with open(self.filepath) as file:
            while True:
                char = file.read(1)
                if char == "\n": break

                for _ in range(int(char)):
                    if is_file:
                        self.disk_map.append(id)
                    else:
                        self.disk_map.append(None)
                    # index += 1
                
                if is_file:
                    id += 1
                is_file = not is_file

        # print(self.disk_map)
    
    def _fill_gaps(self):
        block_i = len(self.disk_map) - 1
        first_free_block_i = self.disk_map.index(None)
        while (first_free_block_i < block_i):
            self.disk_map[first_free_block_i], self.disk_map[block_i] = self.disk_map[block_i], self.disk_map[first_free_block_i]
            first_free_block_i = self.disk_map.index(None)
            self.disk_map.pop(block_i)
            block_i -= 1
        # print(first_free_block_i)
        # self.disk_map = self.disk_map[:first_free_block_i]
        # print(self.disk_map)
    
    def get_check_sum(self):
        sum = 0
        for i in range(len(self.disk_map)):
            sum += (i * self.disk_map[i])
        return sum


if __name__ == "__main__":
    filepath = "./input.txt"
    day9 = Day9(filepath)
    print(f"Part 1: {day9.get_check_sum()}")