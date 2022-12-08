class Stack:
  def __init__(self):
    self._values = []

  def peek(self):
    return self._values[len(self._values)-1]

  def pop(self):
    return self._values.pop()

  def pop_multiple(self, count):
    return [self._values.pop() for i in range(0, count)]

  def push(self, crate):
    self._values.append(crate)

  def push_multiple(self, values):
    for v in values:
      self._values.append(v)

def process_lines_to_crate_list(lines):
  result = []
  for line in lines:
    row = []
    for i in range(1, len(line)-1, 4):
      row.append(line[i])
    result.append(row)
  return result

def parse_crate_stack(lines):
  last_line = lines[len(lines)-1].rstrip()
  stack_count = int(last_line.rstrip()[len(last_line)-1])
  lines_to_process = lines[:len(lines)-1]

  crate_list = process_lines_to_crate_list(lines_to_process)
  crate_list.reverse()  

  stacks = []
  for i in range(0, stack_count):
    stacks.append(Stack())

  for row in crate_list:
    for i, v in enumerate(row):
      if v == " ":
        continue
      stacks[i].push(v)
  return stacks

def parse_movement(lines):
  result = []

  for line in lines:
    value = line.split(" ")
    move_cnt = int(value[1])
    move_src = int(value[3])
    move_dst = int(value[5])
    result.append((move_cnt, move_src, move_dst))
  return result
      

def part_1(stacks, moves):
  for move in moves:
    cnt, src, dst = move
    values = stacks[src-1].pop_multiple(cnt)
    stacks[dst-1].push_multiple(values)

  result = ""
  for stack in stacks:
    result += stack.peek()
  return result

def part_2(stacks, moves):
  for move in moves:
    cnt, src, dst = move
    values = stacks[src-1].pop_multiple(cnt)
    values.reverse()
    stacks[dst-1].push_multiple(values)

  result = ""
  for stack in stacks:
    result += stack.peek()
  return result
   
def read_file(path):
  with open(path) as f:
    return [line.rstrip() for line in f.readlines()]


if __name__ == "__main__":  
  lines = read_file("input.txt")

  # Create crate stack input
  crate_stack_input = []
  for line in lines:
    if line == "":
      break
    crate_stack_input.append(line)

  # Process the crate stack input
  stacks = parse_crate_stack(crate_stack_input)
  moves = parse_movement(lines[len(crate_stack_input)+1:])
  print(part_1(stacks, moves))

  # Process the crate stack input
  stacks = parse_crate_stack(crate_stack_input)
  moves = parse_movement(lines[len(crate_stack_input)+1:])
  print(part_2(stacks, moves))
