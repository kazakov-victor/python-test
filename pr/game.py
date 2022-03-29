import logger


class Game:
    __board = []
    __next_char = ''
    __players = {'x': '', 'o': ''}
    __is_first_player = True
    __cell_counter = 0
    __board_size = len(__board)
    log = logger.Logger

    def __init__(self):
        self.__board = []
        self.__next_char = 'o'
        self.__players = {'x': '', 'o': ''}
        self.__is_first_player = True
        self.__cell_counter = 0
        self.__board_size = len(self.__board)

    def play_game(self):
        self.log.log_to_file('Start of game!')
        next_game = True

        while next_game:
            self.__prepare_game()
            self.__round_game()
            answer = input('New game? (Y/N) ')
            if answer != 'Y' and answer != 'y':
                next_game = False

        self.log.log_to_file('Game is over!')

    def __round_game(self):
        self.log.log_to_file('New round!')
        next_round = True

        while next_round:
            self.__play_round()
            answer = input('New round? (Y/N) ')
            if answer != 'Y' and answer != 'y':
                next_round = False
            else:
                self.__prepare_round()

        self.log.log_to_file('Round is over!')

    def __play_round(self):
        is_round_over = False

        while not is_round_over:
            char = self.__get_next_char()
            column, row = self.__next_step()
            self.__set_cell_value(char, column, row)
            is_round_over = self.__is_round_over(char, column, row)
            self.log.show_board(self.__board)

    def __prepare_game(self):
        self.__set_players_name()
        self.__board_size = self.__get_value('Input board size more than 2: ', 2)
        self.__prepare_round()

    def __prepare_round(self):
        self.__board = []
        self.__board = self.__create_board(self.__board_size)
        self.__cell_counter = self.__board_size * self.__board_size
        self.__is_first_player = True

    def __set_players_name(self):
        print('Hi! Let\'s play!')
        self.__players['x'] = input('Input first player name (it will play with x): ')
        self.__players['o'] = input('Input second player name (it will play with o): ')

    @staticmethod
    def __get_value(message, down_board, up_board=20):
        is_incorrect_input = True
        player_input = 0
        while is_incorrect_input:
            try:
                player_input = int(input(message))
            except ValueError:
                print('Incorrect input!')
            else:
                if player_input < down_board or player_input > up_board:
                    print('Incorrect value!')
                else:
                    is_incorrect_input = False

        return player_input

    def __get_next_char(self):
        if self.__is_first_player:
            next_char = 'x'
        else:
            next_char = 'o'
        self.__is_first_player = not self.__is_first_player
        self.__next_char = next_char
        return next_char

    def __create_board(self, size=3):
        for i in range(size):
            self.__board.append([' '] * size)
        return self.__board

    def __next_step(self):
        print('Step of ' + self.__players[self.__next_char])
        row = self.__get_value('Enter row position from 1 till ' + str(len(self.__board)) + ': ', 1,
                               len(self.__board)) - 1
        column = self.__get_value('Enter column position from 1 till ' + str(len(
            self.__board)) + ': ', 1, len(self.__board)) - 1
        return column, row

    def __set_cell_value(self, value, column, row):
        if self.__check_cell(column, row):
            self.__set_cell(value, column, row)
            self.__cell_counter -= 1
        else:
            self.__get_next_char()
            print('Wrong position!')

    def __check_cell(self, column, row):
        return self.__board[column][row] == ' '

    def __set_cell(self, value, column, row):
        self.__board[column][row] = value

    def __is_round_over(self, char, column, row):
        return self.__check_lines(char, column, row) \
               or self.__check_diagonals(char, column, row) or self.__check_full()

    def __check_lines(self, char, column, row):
        result_column = self.__check_column(char, column)
        result_row = self.__check_row(char, row)

        if result_column or result_row:
            self.log.log_to_file(self.__players[self.__next_char] + ' won!')
            return True
        return False

    def __check_row(self, char, row):
        for column in range(len(self.__board)):
            if self.__board[column][row] != char:
                return False

        return True

    def __check_column(self, char, column):
        for row in range(len(self.__board)):
            if self.__board[column][row] != char:
                return False

        return True

    def __check_diagonals(self, char, column, row):
        diagonal_left = False
        diagonal_right = False

        if column == row:
            diagonal_left = self.__check_diagonal_1(char)

        if row + column == len(self.__board) - 1:
            diagonal_right = self.__check_diagonal_2(char)

        if diagonal_left or diagonal_right:
            self.log.log_to_file(self.__players[self.__next_char] + ' won!')
        return diagonal_left or diagonal_right

    def __check_diagonal_1(self, char):
        for i in range(len(self.__board)):
            if self.__board[i][i] != char:
                return False

        return True

    def __check_diagonal_2(self, char):
        for i in range(len(self.__board)):
            if self.__board[i][len(self.__board) - 1 - i] != char:
                return False
        return True

    def __check_full(self):
        if self.__cell_counter == 0:
            self.log.log_to_file('Nobody won!')
        return self.__cell_counter == 0
