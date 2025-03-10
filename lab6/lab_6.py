with open("input_6.txt", "r") as file:
    lines = file.readlines()

shape_score = {'X': 1, 'Y': 2, 'Z': 3}
outcome_score = {
    ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,  
    ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,  
    ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3   
}

def calculate_total_score(commands):
    total_score = 0
    for command in commands:
        opponent, player = command.strip().split()
        total_score += shape_score[player] + outcome_score[(opponent, player)]
    return total_score

total_score = calculate_total_score(lines)

print("Загальний бал за стратегією:", total_score)
