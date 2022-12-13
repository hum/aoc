def read_file(path):
    with open(path) as f:
        return [line.rstrip() for line in f.readlines()]

def part_1(input_data):
    subset_count = 0
    for section in input_data:
        elf_section_1, elf_section_2 = section.split(",")

        # normalize first elf sectors
        elf1_min, elf1_max = elf_section_1.split("-")
        elf1_min, elf1_max = int(elf1_min), int(elf1_max)

        # normalize second elf sectors
        elf2_min, elf2_max = elf_section_2.split("-")
        elf2_min, elf2_max = int(elf2_min), int(elf2_max)

        elf1 = set(range(elf1_min, elf1_max+1))
        elf2 = set(range(elf2_min, elf2_max+1))

        if elf1.issuperset(elf2) or elf2.issuperset(elf1):
            subset_count += 1

    return subset_count

def part_2(input_data):
    overlap_count = 0
    for section in input_data:
        elf_section_1, elf_section_2 = section.split(",")

        # normalize first elf sectors
        elf1_min, elf1_max = elf_section_1.split("-")
        elf1_min, elf1_max = int(elf1_min), int(elf1_max)

        # normalize second elf sectors
        elf2_min, elf2_max = elf_section_2.split("-")
        elf2_min, elf2_max = int(elf2_min), int(elf2_max)

        elf1 = set(range(elf1_min, elf1_max+1))
        elf2 = set(range(elf2_min, elf2_max+1))

        if elf1.intersection(elf2):
            overlap_count += 1

    return overlap_count

if __name__ == "__main__":  
  lines = read_file("input.txt")
  print(part_1(lines))
  print(part_2(lines))
