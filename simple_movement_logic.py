from checkers_funcs import choose_pieces_color, validation_loop

board = [['r', ' ', 'r', ' ', 'r', ' ', 'r', ' '],
             [' ', 'r', ' ', 'r', ' ', 'r', ' ', 'r'],
             ['r', ' ', 'r', ' ', 'r', ' ', 'r', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
             ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
             [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b']]

pieces_dict = {"r": 12, "b": 12}

user_piece = choose_pieces_color(pieces_dict)

while True:

    for row in board:
        print(row)

    row_index = validation_loop(board, "please enter your chosen row from 0-7.\n", "board", user_piece)
    row = board[row_index]
    row.append("<--")
    for r in board:
        print(r)

    piece_index = validation_loop(row, "please choose a piece on this row.\n", "row", user_piece)
    row[piece_index] += "<-"

    if user_piece == "r":
        next_row = board[row_index+1]
    else:
        next_row = board[row_index-1]
    row.remove("<--")
    next_row.append("<--")
    for r in board:
        print(r)
    next_row_index = validation_loop(next_row, "please choose where you want to move your piece, from 0-7.\n", "next_row", user_piece)
    next_row[next_row_index] = user_piece
    row[piece_index] = " "
    next_row.remove("<--")
