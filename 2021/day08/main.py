#!/usr/bin/python3
import itertools

ALL_VALUES = "abcdefg"
digits = [
	"abcefg",
	"cf",
	"acdeg",
	"acdfg",
	"bcdf",
	"abdfg",
	"abdefg",
	"acf",
	"abcdefg",
	"abcdfg",
]

def sum_output(output, trans):
	result = 0
	for i, j in zip(output, (1000, 100, 10, 1)):
		result += digits.index(translate(i, trans)) * j
	return result

def translate(v, trans):
	return "".join(sorted(v.translate(trans)))

def is_equal(signal, trans):
	return set(digits) == {translate(x, trans) for x in signal}

def part_1(data):
	count = 0
	for results in data.values():
		values = results["output"].split(" ")
		for v in values:
			if len(v) in [2, 3, 4, 7]:
				count += 1
	return count

def part_2(data):
	count = 0
	for k, v in data.items():
		for perm in itertools.permutations(ALL_VALUES):
			trans = str.maketrans(ALL_VALUES, "".join(perm))
			if is_equal(v["signal"].split(" "), trans):
				count += sum_output(v["output"].split(" "), trans)
				break

	return count
	

if __name__ == "__main__":
	with open("./input", "r") as f:
		data = {}
		for i, line in enumerate(f.readlines()):
			line = line.strip().split(" | ")
			data[i] = {"signal": line[0], "output": line[1]}
		
		print(part_1(data))
		print(part_2(data))
