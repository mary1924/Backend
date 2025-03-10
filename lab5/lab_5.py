def parse_game_data(game_data):
    games = []
    for line in game_data:
        id, sets = line.split(':')
        id = int(id.strip().split()[-1])
        sets = [s.strip().split(',') for s in sets.split(';')]
        sets = [{c.strip().split()[1]: int(c.strip().split()[0]) for c in s} for s in sets]
        games.append((id, sets))
    return games

def is_game_possible(game_sets, max_cubes):
    current_cubes = {color: 0 for color in max_cubes.keys()}
    for game_set in game_sets:
        for color, count in game_set.items():
            current_cubes[color] += count
            if current_cubes[color] > max_cubes[color]:
                return False
        for color in max_cubes.keys():
            current_cubes[color] = 0 
    return True

def main():
    with open('input_5.txt', 'r') as file:
        game_data = file.readlines()

    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    games = parse_game_data(game_data)
    possible_games_ids = [game_id for game_id, game_sets in games if is_game_possible(game_sets, max_cubes)]

    print("Можливі ігри: ", possible_games_ids)
    print("Сума ID можливих ігор: ", sum(possible_games_ids))

if __name__ == "__main__":
    main()
