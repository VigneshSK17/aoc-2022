def get_ranges(file_name):

    ranges = []

    with open(file_name) as f:
        for line in f.readlines():
            line_ranges = line.split(',')

            s11, s12 = line_ranges[0].split('-')
            s21, s22 = line_ranges[1].split('-')
            set_1 = set(range(int(s11), int(s12) + 1))
            set_2 = set(range(int(s21), int(s22) + 1))

            ranges.append((set_1, set_2))

    return ranges

def overlapping_ranges(file_name):
    ranges = get_ranges(file_name)
    return sum([1 for s1, s2 in ranges if s2.issubset(s1) or s1.issubset(s2)])

def overlapping_part_ranges(file_name):
    ranges = get_ranges(file_name)
    return sum([1 for s1, s2 in ranges if not s1.isdisjoint(s2)])

print(overlapping_ranges("./d4/input.txt"))
print(overlapping_part_ranges("./d4/input.txt"))

