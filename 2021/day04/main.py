#!/usr/bin/python3
from collections import defaultdict

BOARD_HEIGHT = 5
BOARD_WIDTH = 5

def num_in_board(num, board):
	for row in board:
		if num in row:
			return True
	return False

def mark_number(num, board):
	for i, row in enumerate(board):
		for j, value in enumerate(row):
			if value == num:
				board[i][j] = "x"
				return board

def is_winner(board):
	winning_row = list("x" * BOARD_WIDTH)
	counted_x = defaultdict(int)

	for row in board:
		if row == winning_row:
			return True

		for i, value in enumerate(row):
			if value == "x":
				counted_x[i] += 1
				if counted_x[i] == BOARD_HEIGHT:
					return True
	return False

def sum_board_values(board):
	result = 0
	for row in board:
		for num in row:
			if num == "x":
				continue
			result += num
	return result
			
def part_1(drawn_numbers, boards):
	for drawn in drawn_numbers:
		for i, board in enumerate(boards):
			if not num_in_board(drawn, board):
				continue
			boards[i] = mark_number(drawn, board)
			if is_winner(board):
				sum_val = sum_board_values(board)
				print(sum_val, drawn)
				return sum_val * drawn

def part_2(drawn_numbers, boards):
	won_boards = []

	for drawn in drawn_numbers:
		for i, board in enumerate(boards):
			if not num_in_board(drawn, board):
				continue
			if board in won_boards:
				continue

			boards[i] = mark_number(drawn, board)
			if is_winner(board):
				if len(won_boards) == len(boards)-1:
					sum_val = sum_board_values(board)
					return sum_val * drawn
				won_boards.append(board)
				continue
				
def format_boards(raw_boards):
	result = []
	tmp = []
	for row in raw_boards:
		if len(tmp) == BOARD_HEIGHT or row == "\n":
			result.append(tmp)
			tmp = []
			continue

		row = row.replace("  ", " ").strip()
		row = row.split(" ")
		r = [int(v.lstrip()) for v in row]
		tmp.append(r)
	result.append(tmp)
	return result

if __name__ == "__main__":
	with open("./input", "r") as f:
		drawn_numbers = [int(v) for v in f.readline().split(",")]
		f.readline()
		raw_boards = [row for row in f.readlines()]
		boards = format_boards(raw_boards)

	print(part_1(drawn_numbers, boards))
	print(part_2(drawn_numbers, boards))
