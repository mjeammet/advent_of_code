f = open('inputs/day02_input','r+')
max_cubes = {"red":12, "green":13, "blue":14}


def first_part():
    total_sum = 0
    
    for line in f:
        game_id, game = line.strip().split(": ")
        is_line_possible = True

        sets = game.split('; ')
        for gameset in sets:
            sets = gameset.split(", ")
            for cubes in sets: 
                value, color = cubes.split(" ")
                if int(value) > max_cubes[color]:
                    is_line_possible = False
            
        if is_line_possible:
            # print("Adding", game_id.strip("Game ") )
            total_sum += int(game_id.strip("Game "))

    return total_sum
    

def second_part():
    total_sum = 0

    for line in f:
        min_cubes = {"red":0, "green":0, "blue":0}
        game_id, game = line.strip().split(": ")

        sets = game.split('; ')
        for gameset in sets:
            sets = gameset.split(", ")
            for cubes in sets: 
                value, color = cubes.split(" ")
                if int(value) > min_cubes[color]:
                    min_cubes[color] = int(value)

        total_sum += min_cubes["red"]*min_cubes["green"]*min_cubes["blue"]

    return total_sum

print(second_part())
