#!/bin/bash/python3

GRID_WIDTH = 1000
GRID_HEIGHT = 1000
EMPTY_VALUE = 0

def view_grid(grid):
	# only works with 10x10 sample grid
	result = ""
	for row in grid:
		result += ' '.join([str(value) if value else "." for value in row]) + "\n"
	return result

def parse_row(row):
	row = row.replace(",", " ").replace(" ->", "").split(" ")
	return [int(v) for v in row]

def count_two_or_more_overlap(grid):
	count = 0
	for row in grid:
		for value in row:
			if not isinstance(value, int):
				continue
			if value >= 2:
				count += 1
	return count

def get_diff_points(x1, y1, x2, y2):
	dx = abs(x2 - x1)
	dy = -abs(y2 - y1)
	sx = 1 if x1 < x2 else -1
	sy = 1 if y1 < y2 else -1
	err = dx + dy

	result = []
	while True:
		result.append((x1, y1))
		if x1 == x2 and y1 == y2:
			break

		ev = err * 2
		if ev >= dy:
			err += dy
			x1 += sx
		
		if ev <= dx:
			err += dx
			y1 += sy
	return result

def walk_vector(grid, x1, y1, x2, y2):
	points = get_diff_points(x1, y1, x2, y2)
	for x, y in points:
		grid[y][x] += 1
	return grid

def part_1(rows):
	grid = [[EMPTY_VALUE] * GRID_WIDTH for i in range(GRID_HEIGHT)]

	for row in rows:
		x1, y1, x2, y2 = parse_row(row)
		if not (x1 == x2 or y1 == y2):
			continue

		grid = walk_vector(grid, x1, y1, x2, y2)

	print(view_grid(grid))
	return count_two_or_more_overlap(grid)

def part_2(rows):
	grid = [[EMPTY_VALUE] * GRID_WIDTH for i in range(GRID_HEIGHT)]

	for row in rows:
		p = parse_row(row)
		gird = walk_vector(grid, *p)

	print(view_grid(grid))
	return count_two_or_more_overlap(grid)

if __name__ == "__main__":
	with open("./input", "r") as f:
		rows = [row.strip() for row in f.readlines()]
		print(part_1(rows))
		print(part_2(rows))
