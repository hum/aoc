from enum import Enum

def read_file(path):
	with open(path) as f:
		return [line.rstrip() for line in f.readlines()]

class Shape(Enum):
	value: str
	Rock = "A"
	Paper = "B"
	Scissors = "C"


shape_to_score = {
	Shape.Rock: 1,
	Shape.Paper: 2,
	Shape.Scissors: 3,
}

p2_shape_mapping = {
	"X": Shape.Rock,
	"Y": Shape.Paper,
	"Z": Shape.Scissors,	
}

win_shape = {
	Shape.Paper: Shape.Scissors,
	Shape.Rock: Shape.Paper,
	Shape.Scissors: Shape.Rock,
}

loss_shape = {
	Shape.Paper: Shape.Rock,
	Shape.Rock: Shape.Scissors,
	Shape.Scissors: Shape.Paper,
}

def part_1(input_data):
	points_win, points_draw, points_loss = 6, 3, 0
	p2_score = 0

	for play_round in input_data:
		p1, p2 = play_round.split(" ")

		# Normalize
		p1 = Shape(p1)
		p2 = p2_shape_mapping[p2]

		# This always happens no matter the outcome
		p2_score += shape_to_score[p2]

		if p1 == p2:
			# draw
			p2_score += points_draw
		elif p1 == win_shape[p2]:
			# P1 wins
			p2_score += points_loss
		else:
			# P2 wins
			p2_score += points_win

	return p2_score

class Outcome(Enum):
	value: str
	Loss = "X"
	Draw = "Y"
	Win = "Z"

def part_2(input_data):
	points_win, points_draw, points_loss = 6, 3, 0
	p2_score = 0

	for play_round in input_data:
		p1, outcome = play_round.split(" ")

		# Normalize
		p1 = Shape(p1)
		outcome = Outcome(outcome)

		if outcome == Outcome.Draw:
			# draw
			p2_score += points_draw + shape_to_score[p1]
		elif outcome == Outcome.Loss:
			# P1 wins
			p2_score += points_loss + shape_to_score[loss_shape[p1]]
		else:
			# P2 wins
			p2_score += points_win + shape_to_score[win_shape[p1]]

	return p2_score

if __name__ == "__main__":	
	lines = read_file("input.txt")
	print(part_1(lines))
	print(part_2(lines))
