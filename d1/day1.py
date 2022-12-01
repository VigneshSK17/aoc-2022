def get_calories(file_name):
    with open(file_name) as f:
        elves = [n.split('\n') for n in f.read().split('\n\n')]  
        elves[-1] = elves[-1][:-1]
        elves_cals = [list(map(lambda x: int(x), n)) for n in elves]
        return [sum(n) for n in elves_cals]

def get_most_calories(elves_cals: list[int]):
    return max(elves_cals)

def get_top_3_elves(elves_cals: list[int]):
    cals = 0
    for _ in range(3):
        cal = get_most_calories(elves_cals)
        elves_cals.remove(cal)
        cals += cal
    return cals
    

print(get_most_calories(get_calories("input.txt")))
print(get_top_3_elves(get_calories("input.txt")))
