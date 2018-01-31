import random
import os
import scenes


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]


def get_location():
    return random.sample(CELLS, 3)


def show_scene(player):
    try:
        print(scenes.scenes[player])
    except KeyError:
        print('You cannot see!')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_moves(player):
    x, y = player
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')
    return moves


def move_player(player, move_input):
    x, y = player
    if move_input == 'LEFT':
        x -= 1
    if move_input == 'RIGHT':
        x += 1
    if move_input == 'UP':
        y -= 1
    if move_input == 'DOWN':
        y += 1
    return x, y


def draw_map(player):
    print("    MAP   ")
    print(" _"*5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)


def game_loop():
    player, monster, door = get_location()

    while True:
        clear_screen()
        print("\n")
        draw_map(player)
        print("\n")

        print("Your current location is: {}".format(player))
        show_scene(player)
        print("\n")
        print("You can currently move: {}".format(', '.join(get_moves(player)).title()))
        move_input = input("> ").upper()
        
        valid_move = get_moves(player)
        if move_input in valid_move:
            player = move_player(player, move_input)
        elif move_input not in valid_move:
            print("Ouch! Walls hurt!")
        elif move_input == 'q':
            print("Goodbye!")
        
        


game_loop()
