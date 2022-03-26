import logger

board = []
next_char = 'o'
players = {'x': '', 'o': ''}
is_first_player = True


def prepare():
    global board
    set_players_name()
    board_size = get_meaning('Input board size more than 2: ', 2)
    board = create_board(board_size)
    logger.show_board(board)


def set_players_name():
    global players
    print('Hi! Let\'s play!')
    players['x'] = input('Input first player name (it will play with x): ')
    players['o'] = input('Input second player name (it will play with o): ')


def get_meaning(message, down_board, up_board=20):
    is_incorrect_input = True
    player_input = 0
    while is_incorrect_input:
        try:
            player_input = int(input(message))
        except ValueError:
            print('Incorrect input!')
        else:
            if player_input < down_board or player_input > up_board:
                print('Incorrect meaning!')
            else:
                is_incorrect_input = False

    return player_input


def get_next_char():
    global is_first_player, next_char
    if is_first_player:
        next_char = 'x'
    else:
        next_char = 'o'
    is_first_player = not is_first_player
    return next_char


def create_board(size=3):
    for i in range(size):
        board.append([' '] * size)
    return board


def next_step():
    print('Next step of ' + players[next_char])
    row = get_meaning('Enter row position from 1 till ' + str(len(board)) + ': ', 1, len(board)) - 1
    column = get_meaning('Enter column position from 1 till ' + str(len(board)) + ': ', 1,
                         len(board)) - 1
    return column, row


def set_cell_meaning(char, column, row):
    if check_cell(column, row):
        set_cell(char, column, row)
    else:
        get_next_char()
        print('Wrong position!')


def check_cell(column, row):
    return board[column][row] == ' '


def set_cell(char, column, row):
    board[column][row] = char


def is_game_over():
    return check_lines() or check_diagonals() or check_full()


def check_lines():
    result = False
    for i in range(len(board)):
        result = check_column(i, result)
        result = check_row(i, result)

    if result:
        logger.log_to_file(players[next_char] + ' won!')
    return result


def check_row(i, result):
    if board[i][0] != ' ':
        check_char = board[i][0]
        counter = 0
        for j in range(len(board[i])):
            if board[i][j] == check_char:
                counter += 1
            else:
                break
        if counter == len(board):
            result = True
    return result


def check_column(i, result):
    if board[0][i] != ' ':
        check_char = board[0][i]
        counter = 0
        for j in range(len(board[i])):
            if board[j][i] == check_char:
                counter += 1
            else:
                break
        if counter == len(board):
            result = True
    return result


def check_diagonals():
    check_char_1 = board[0][0]
    check_char_2 = board[0][len(board) - 1]
    counter_1 = 0
    counter_2 = 0

    for i in range(len(board)):
        if check_char_1 != ' ' and board[i][i] == check_char_1:
            counter_1 += 1
        if check_char_2 != ' ' and board[i][len(board) - 1 - i] == check_char_2:
            counter_2 += 1

    if (counter_1 == len(board)) or (counter_2 == len(board)):
        logger.log_to_file(players[next_char] + ' won!')
    return (counter_1 == len(board)) or (counter_2 == len(board))


def check_full():
    counter = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' ':
                counter += 1

    if counter == 0:
        logger.log_to_file('Nobody won!')
    return counter == 0
