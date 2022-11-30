#!/usr/bin/python3

def find_most_common_binary_number(rows, index):
	count = 0
	for row in rows:
		if int(row[index]) > 0:
			count += 1
	return 1 if count > (len(rows)-1)//2 else 0

def filter_values(arr, f, index):
	result = []
	for v in arr:
		if v[index] == f:
			result.append(v)
	return result

def part_1(rows):
	gamma, epsilon = "", ""
	for i in range(0, len(rows[0])):
		most_common = find_most_common_binary_number(rows, i)
		gamma += str(most_common)
		epsilon += "0" if most_common else "1"
	return int(gamma, 2) * int(epsilon, 2)

def part_2(rows):
	oxygen, co2 = rows, rows

	for i in range(0, len(rows[0])):
		if not len(oxygen) == 1:
			most_common = find_most_common_binary_number(oxygen, i)
			oxygen = filter_values(oxygen, str(most_common), i)
		if not len(co2) == 1:
			most_common = "0" if find_most_common_binary_number(co2, i) else "1"
			co2 = filter_values(co2, most_common, i)	
	return int(oxygen[0], 2) * int(co2[0], 2)

if __name__ == "__main__":
	with open("./input", "r") as f:
		data = [row.strip("\n") for row in f.readlines()]
		print(part_1(data))
		print(part_2(data))
