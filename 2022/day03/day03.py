from collections import defaultdict

points = {}

# lowercase letters
letter_points = 1
for letter in range(97, 123):
	points[chr(letter)] = letter_points	
	letter_points += 1

# uppercase letters
letter_points = 27
for letter in range(65, 91):
	points[chr(letter)] = letter_points	
	letter_points += 1

def part_1(input_data):
	priority_sum = 0
	
	for rucksack in input_data:
		half_size = len(rucksack) // 2

		comp1, comp2 = rucksack[:half_size], rucksack[half_size:]

		# hacky removal of recurring chars
		comp1 = "".join(list(set(comp1)))
		comp2 = "".join(list(set(comp2)))

		for i in range(0, len(comp1)):
			letter = comp1[i]
			if not letter in comp2:
				continue

			priority_sum += points[letter]
	return priority_sum


def part_2(input_data):
	priority_sum = 0
	for i in range(0, len(input_data), 3):
		r1, r2, r3 = input_data[i], input_data[i+1], input_data[i+2]
		common = set(r1) & set(r2) & set(r3)
		common_letter = list(common)[0]
		priority_sum += points[common_letter]

	return priority_sum
		

def read_file(path):
	with open(path) as f:
		return [line.rstrip() for line in f.readlines()]


if __name__ == "__main__":	
	lines = read_file("input.txt")
	print(part_1(lines))
	print(part_2(lines))
