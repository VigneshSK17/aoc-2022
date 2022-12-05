def get_crates(file_name):
    crates_str = []

    with open(file_name) as f:
        for line in f.readlines():
            if line == '\n':
                break
            crates_str.append(line)

    count = int(crates_str[-1][-3])
    height = len(crates_str) - 1
    crates = [[]]


    for i in range(count):
        index = (4 * i) + 1
        crates.append([])
        for line in crates_str[:-1]:
            if line[index] != " ":
                crates[-1].append(line[index])
            else:
                crates[-1].append(None)

    return crates, height

def parse_instructions(file_name, start):
    instructions = []
    with open(file_name) as f:
        for line in f.readlines()[start + 2:]:
            s = line.split(' ')
            instructions.append((int(s[1]), int(s[3]), int(s[5])))

    return instructions

def move_stack(crates, instruction):
    count, orig, new = instruction

    for _ in range(count):
        i, crate_val = next((i, crate) for (i, crate) in enumerate(crates[orig]) if crate is not None)
        crates[orig][i] = None

        if None not in crates[new]:
            crates[new].insert(0, crate_val)
        else:
            new_i = len(crates[new]) - crates[new][::-1].index(None) - 1
            crates[new][new_i] = crate_val

    return crates

def move_stack_retain_order(crates, instruction):
    count, orig, new = instruction
    moved_crates = []

    for _ in range(count):
        i, crate_val = next((i, crate) for (i, crate) in enumerate(crates[orig]) if crate is not None)
        moved_crates.append(crate_val)
        crates[orig][i] = None

    for crate in moved_crates[::-1]:
        if None not in crates[new]:
            crates[new].insert(0, crate)
        else:
            new_i = len(crates[new]) - crates[new][::-1].index(None) - 1
            crates[new][new_i] = crate

    return crates


def rearrange_stacks(file_name, move_stack_function):
    crates, height = get_crates(file_name)
    instructions = parse_instructions(file_name, height)

    for instruction in instructions:
        crates = move_stack_function(crates, instruction)

    ans = ""
    for crate in crates[1:]:
        crate_val = next(c for c in crate if c is not None)
        ans += crate_val
    return ans 

file_name = "./d5/input.txt"
print(rearrange_stacks(file_name, move_stack))
print(rearrange_stacks(file_name, move_stack_retain_order))