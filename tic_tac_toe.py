"""
tic_tac_toe.py: druhý projekt do Engeto Online Python Akademie
author: Jan Pavlík
email: Jan.Pavlik@rmgastro.com
discord: Jan P.#7609
"""

# Constant
separators_length = 40
separator_equal = '=' * separators_length
separator_dash = '-' * separators_length
board = [" " for x in range(9)]


def print_board():
    """"
    Definice hracího pole
    """
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print('+---+---+---+')
    print(row1)
    print(row2)
    print(row3)
    print('+---+---+---+')


def player_move(icon):
    """"
    Definice hráčského tahu
    """
    while True:
        print(separator_equal)
        print("Player {}".format(icon))
        choice = input("| Please enter your move number: ")
        print(separator_equal)

        if choice.isnumeric():
            if int(choice) in range(1, 10):
                if board[int(choice) - 1] == " ":
                    board[int(choice) - 1] = icon
                    break
                else:
                    print('The entered position already occupied!')
            else:
                print('The entered value not in range!')
        else:
            print("The entered value is not a number!")


def is_victory(icon):
    """"
    Kontrola, zda-li hráč vyhrál
    """
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    """"
    Kontrola, zda-li není remíza
    """
    if " " not in board:
        return True
    else:
        return False


# Main
print(
    "Welcome to Tic Tac Toe",
    separator_equal,
    "GAME RULES:",
    "Each player can place one mark (or stone)",
    "per turn on the 3x3 grid. The WINNER is",
    "who succeeds in placing three of their",
    "marks in a:",
    "* horizontal,",
    "* vertical or",
    "* diagonal row",
    separator_equal,
    "Let's start the game",
    separator_dash,
    sep="\n")

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print(separator_equal, "Congratulations, the player x WON!", separator_equal, sep="\n")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print(separator_equal, "Congratulations, the player o WON!", separator_equal, sep="\n")
        break
    elif is_draw():
        print("It's a draw!")
        break