def read_file(path):
    with open(path) as f:
        return [line.rstrip() for line in f.readlines()]

def is_unique(values):
	return len(set(values)) == len(values)

def move_window(line, offset):
	for idx in range(0, len(line)):
		end_idx = idx + offset	
		values = line[idx:end_idx]
		if not is_unique(values):
			continue	

		return end_idx

def part_1(lines):
	# File has only one line
	line = lines[0]	

	offset = 4
	idx = move_window(line, offset)
	return idx

def part_2(lines):
	# File has only one line
	line = lines[0]	

	offset = 14
	idx = move_window(line, offset)
	return idx

if __name__ == "__main__":  
  lines = read_file("input.txt")
  print(part_1(lines))
  print(part_2(lines))
