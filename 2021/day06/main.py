#!/usr/bin/python3
from collections import Counter

def do_cycle(c):
	count = Counter()

	for i in range(8):
		count[i] = c[i+1]

	count[6] += c[0]
	count[8] += c[0]
	return count

def part_1(days, lf):
	counter = Counter(lf)

	for day in range(days):
		counter = do_cycle(counter)
	return sum(counter.values())

if __name__ == "__main__":
	with open("./input", "r") as f:
		states = next(f).strip()
		states = states.split(",")
		init_state = [int(v) for v in states]
		print(part_1(80, init_state))
		print(part_1(256, init_state))
