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
    print(game_over_messages(grid_data, current_player))
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

    has_winner = has_a_line(grid_data)

    return full_selection == False and has_winner == False

def has_a_line(grid_data):
    return (grid_data[0] == grid_data[1] == grid_data[2] or
            grid_data[3] == grid_data[4] == grid_data[5] or
            grid_data[6] == grid_data[7] == grid_data[8] or
            grid_data[0] == grid_data[3] == grid_data[6] or
            grid_data[1] == grid_data[4] == grid_data[7] or
            grid_data[2] == grid_data[5] == grid_data[8] or
            grid_data[0] == grid_data[4] == grid_data[8] or
            grid_data[2] == grid_data[4] == grid_data[6])

def get_color(player):
    if player == "x":
        return "blue"
    else:
        return "green"

def game_over_messages(grid_data, player):
    player = next_player(player)
    color = get_color(player)
    if has_a_line(grid_data) == True:
        return colored(f"Player \"{player}\" won the game.", color)
    else:
        return "The game ended in a draw."

if __name__ == "__main__":
    main()