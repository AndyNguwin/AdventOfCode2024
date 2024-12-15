class Day9:
    def __init__(self, filepath):
        # MAYBE CONVERT TO JUST A DICTIONARY FOR THE DISK MAP
        # Track only the indexes of the file blocks associated to ID
        # Free block lengths can be determined by subtracting the block indexes
        self.filepath = filepath
        self.disk_map = []
        self.free_block_starts = []
        self.free_block_lengths = dict()
        self.file_block_lengths = dict()
    
    def _convert_disk_map(self):
        self.disk_map = []
        is_file = True
        id = 0
        with open(self.filepath) as file:
            while True:
                char = file.read(1)
                if char == "\n": break
                start_index = len(self.disk_map) - 1

                for _ in range(int(char)):
                    if is_file:
                        self.disk_map.append(id)
                    else:
                        self.disk_map.append(None)
                
                if is_file:
                    self.file_block_lengths[id] = int(char)
                    id += 1
                else:
                    self.free_block_starts = start_index
                    self.free_block_lengths[start_index] = int(char)

                is_file = not is_file
    
    def _fill_gaps(self, part):
        if part == 1:
            block_i = len(self.disk_map) - 1
            first_free_block_i = self.disk_map.index(None)
            while (first_free_block_i < block_i):
                self.disk_map[first_free_block_i], self.disk_map[block_i] = self.disk_map[block_i], self.disk_map[first_free_block_i]
                first_free_block_i = self.disk_map.index(None)
                self.disk_map.pop(block_i)
                block_i -= 1

        if part == 2:
            pass
            
    
    def get_checksum(self, part):
        self._convert_disk_map()
        self._fill_gaps(part)
        sum = 0
        for i in range(len(self.disk_map)):
            sum += (i * self.disk_map[i])
        return sum


if __name__ == "__main__":
    filepath = "./input.txt"
    day9 = Day9(filepath)
    print(f"Part 1: {day9.get_checksum(1)}")