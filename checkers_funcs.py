import random


def choose_pieces_color(options):
    user_piece = input("please choose your color.\n"
                       "'b' = black, 'r' = red\n"
                       "If you type anything other than 'b' or 'r',\n"
                       "the color of your pieces will be decided randomly.\n")
    if user_piece not in options.keys():
        user_piece = random.choice(list(options.keys()))
    print(f"You chose the color {user_piece}")
    return user_piece


def is_valid(list_to_validate, message, name_of_list, piece_color):
    try:
        player_input = int(input(message))
    except ValueError:
        print("Sorry, you can't input letters.\nPlease try again")
        return False
    try:
        list_to_validate[player_input]
    except IndexError:
        print(f"The value {player_input} doesn't exist.\nPlease try again")
        return False

    if name_of_list == "board" and piece_color not in list_to_validate[player_input]:
        print(f"Your pieces color is \"{piece_color}\",\n"
              f"the row you chose doesn't have any pieces \"{piece_color}\" in it.\n"
              f"Please choose a row that has the pieces \"{piece_color}\".")
        return False

    if name_of_list == "row" and list_to_validate[player_input] != piece_color:
        print(list_to_validate)
        print(f"You can't choose this piece."
              f"\nYou can only choose the pieces of your own color, {piece_color}")
        return False

    if name_of_list == "next_row" and list_to_validate[player_input] != " ":
        print("Pieces can only be placed on empty spaces.")
        return False

    return player_input, True


def validation_loop(list_to_validate, message, name_of_list, piece_color):
    while True:
        user_input = is_valid(list_to_validate, message, name_of_list, piece_color)
        if user_input:
            break
    return user_input[0]
#
# def movement(next_row, message):
#     user_input = int(input(message))
#     print(placement)
#     if placement > len(board):
#         print("you can't place your piece here. There's no such number on the board")
#         break
#     if board[placement] != "":
#         print("You can't place your piece here. There is another piece in this place")
#         break
#     board[placement] = piece
#     print(board)
#     return

