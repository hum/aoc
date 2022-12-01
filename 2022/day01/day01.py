def read_file(path):
	with open("input.txt") as f:
		return [line.rstrip() for line in f.readlines()]
		

if __name__ == "__main__":
	input_data = read_file("input.txt")

	elfs, tmp = [], 0
	for line in input_data:
		if not line:
			elfs.append(tmp)
			tmp = 0
			continue

		tmp += int(line)

	elfs.sort(reverse=True)

	# Part 1
	print(elfs[0])

	# Part 2
	print(elfs[0] + elfs[1] + elfs[2])
