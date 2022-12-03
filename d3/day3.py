def open_file_rucksacks(file_name):
    with open(file_name) as f:
        return [(l[:len(l)//2], l[len(l)//2:]) for l in f.readlines()]

def open_file_groups(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        return [lines[i:i + 3] for i in range(0, len(lines), 3)]

def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

def get_all_priorities(file_name):
    rucksacks = open_file_rucksacks(file_name)

    priorities = 0
    for rucksack in rucksacks:
        for c in rucksack[0]:
            if c in rucksack[1]:
                priorities += get_priority(c)
                break

    return priorities

def get_groups_priorities(file_name):
    groups = [''.join(group) for group in open_file_groups(file_name)]

    priorities = 0

    for group in groups:
        rucksacks = group.split('\n')
        for c in rucksacks[0]:
            if c in rucksacks[1] and c in rucksacks[2]:
                priorities += get_priority(c)
                break

    return priorities

print(get_all_priorities('./d3/input.txt'))
print(get_groups_priorities('./d3/input.txt'))