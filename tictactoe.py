'''
Assignment: Tic-Tac-Toe
Author: Edgar Valderrama
'''

from termcolor import colored, cprint

def main():
    grid_data = list(range(1, 10))
    current_player = "x"

    while open_game(grid_data):
        display_grid(grid_data)

        text = f"{current_player}'s turn to choose a square (1-9): "
        color = get_color(current_player)

        square = int(input(colored(text, color)))
        grid_data[square - 1] = current_player

        current_player = next_player(current_player)

    display_grid(grid_data)
    print("Good game. Thanks for playing!")

def next_player(player):
    if player == "x":
        return "o"
    else:
        return "x"

def display_grid(grid_data):
    print()
    print(f"{grid_data[0]}|{grid_data[1]}|{grid_data[2]}")
    print('-+-+-')
    print(f"{grid_data[3]}|{grid_data[4]}|{grid_data[5]}")
    print('-+-+-')
    print(f"{grid_data[6]}|{grid_data[7]}|{grid_data[8]}")
    print()

def open_game(grid_data):
    full_selection = True
    for i in range(9):
        if grid_data[i] != "x" and grid_data[i] != "o":
            full_selection = False

    has_a_line = (grid_data[0] == grid_data[1] == grid_data[2] or
                  grid_data[3] == grid_data[4] == grid_data[5] or
                  grid_data[6] == grid_data[7] == grid_data[8] or
                  grid_data[0] == grid_data[3] == grid_data[6] or
                  grid_data[1] == grid_data[4] == grid_data[7] or
                  grid_data[2] == grid_data[5] == grid_data[8] or
                  grid_data[0] == grid_data[4] == grid_data[8] or
                  grid_data[2] == grid_data[4] == grid_data[6])

    return full_selection == False and has_a_line == False

def get_color(player):
    if player == "x":
        return "blue"
    else:
        return "green"

if __name__ == "__main__":
    main()