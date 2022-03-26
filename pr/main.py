import logger
import game

next_game = True
game.prepare()


def play():
    logger.log_to_file('Start of game!')

    while not game.is_game_over():
        char = game.get_next_char()
        column, row = game.next_step()
        game.set_cell_meaning(char, column, row)
        logger.show_board(game.board)

    logger.log_to_file('Game is over!')


while next_game:

    play()
    answer = input('Repeat? Y/N ')
    if answer != 'Y' and answer != 'y':
        next_game = False
