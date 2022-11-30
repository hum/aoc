#!/usr/bin/python3

FORWARD = "forward"
DOWN = "down"
UP = "up"

def get_commands(filename: str):
	values = []
	with open(filename, "r") as f:
		values = [row for row in f.readlines()]

	result = []
	for row in values:
		cmd, value = row.split(" ")
		value = int(value)
		result.append((cmd, value))
	return result
			

def part_1():
	x, y = 0, 0
	commands = get_commands("./input")

	for cmd, value in commands:
		if cmd == FORWARD:
			x += value
		elif cmd == DOWN:
			y += value
		elif cmd == UP:
			y -= value
	return x*y

def part_2():
	x, y, aim = 0, 0, 0
	commands = get_commands("./input")

	for cmd, value in commands:
		if cmd == DOWN:
			aim += value
		elif cmd == UP:
			aim -= value
		elif cmd == FORWARD:
			x += value
			y += value * aim

	return x*y
		
if __name__ == "__main__":
	print(part_1())
	print(part_2())
