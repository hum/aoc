#!/usr/bin/python3

def part_1():
  count, last = 0, None

  with open("./input", "r") as f:
    last = int(next(f))

    for line in f:
      v = int(line)
      if v > last:
        count += 1
      last = v
    return count

def part_2():
  count, last, p = 0, 0, 0
  values = []

  with open("./input", "r") as f:
    values = [int(v) for v in f.readlines()]
    while p < len(values)-2:
      v = values[p] + values[p+1] + values[p+2]
      if v > last:
        count += 1
      last = v
      p += 1
  return count-1


if __name__ == "__main__":
  print(part_1())
  print(part_2())
      
