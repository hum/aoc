#!/usr/bin/python3
import statistics
import math

def find_fuel_value(crabs, y):
	fuel = 0
	for crab in crabs:
		fuel += abs(crab - y)
	return fuel

def find_fuel_exp_value(crabs, y):
	fuel = 0
	for crab in crabs:
		steps = abs(crab - y)
		fuel += (steps * (steps + 1))//2
	return fuel

def part_1(pos):
	crabs = pos
	crabs.sort()

	min_val = math.inf
	for y in range(max(crabs)):
		curr_fuel = find_fuel_value(crabs, y)
		if curr_fuel < min_val:
			min_val = curr_fuel
	return min_val

def part_2(pos):
	crabs = pos
	crabs.sort()
	
	min_val = math.inf
	for y in range(max(crabs)):
		curr_fuel = find_fuel_exp_value(crabs, y)
		if curr_fuel < min_val:
			min_val = curr_fuel
	return min_val

if __name__ == "__main__":
	with open("./input", "r") as f:
		data = [int(v) for v in f.readline().split(",")]
		print(part_1(data))
		print(part_2(data))
