
def open_file(file_name):
    with open(file_name) as f:
        return [outcomes.strip().split(' ') for outcomes in f.readlines()]

def get_total_score(outcomes):
    total_score = 0
    you_score = {'X': 1, 'Y': 2, 'Z': 3}
    their_equiv = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    their_outcome = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    for [o, y] in outcomes:
        total_score += you_score[y] 
        if y == their_outcome[o]:
            total_score += 6
        elif y == their_equiv[o]:
            total_score += 3

    return total_score

def get_predicted_score(outcomes):
    win_outcome = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    draw_outcome = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    lose_outcome = {'A': 'Z', 'B': 'X', 'C': 'Y'}

    predicted_outcomes = []
    for [o, y] in outcomes:
        if y == 'X':
            predicted_outcomes.append([o, lose_outcome[o]])
        elif y == 'Y':
            predicted_outcomes.append([o, draw_outcome[o]])
        else:
            predicted_outcomes.append([o, win_outcome[o]])

    return get_total_score(predicted_outcomes)


print(get_total_score(open_file("./d2/input.txt")))
print(get_predicted_score(open_file("./d2/input.txt")))
