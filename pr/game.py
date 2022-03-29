import logger


class Game:
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

        while True:
            self.__prepare_game()
            self.__round_game()
            if input('New game? Y/(N or other char): ').lower() != 'y':
                break

        self.log.log_to_file('Game is over!')

    def __round_game(self):
        self.log.log_to_file('New round!')

        while True:
            self.__play_round()
            if input('New round? Y/(N or other char): ').lower() != 'y':
                break
            else:
                self.__prepare_round()

        self.log.log_to_file('Round is over!')

    def __play_round(self):
        while True:
            char = self.__get_next_char()
            column, row = self.__next_step()
            self.__set_cell_value(char, column, row)
            self.log.show_board(self.__board)
            if self.__is_round_over(char, column, row):
                break

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
        self.__players['x'] = input('Input name of first player: ')
        self.__players['o'] = input('Input name of second player: ')

    @staticmethod
    def __get_value(message, down_board, up_board=20):
        while True:
            try:
                player_input = int(input(message))
            except ValueError:
                print('Incorrect input!')
            else:
                if player_input < down_board or player_input > up_board:
                    print('Incorrect value!')
                else:
                    break

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
            print('Wrong position. Try again!')

    def __check_cell(self, column, row):
        return self.__board[column][row] == ' '

    def __set_cell(self, value, column, row):
        self.__board[column][row] = value

    def __is_round_over(self, char, column, row):
        if self.__check_lines(char, column, row) or self.__check_diagonals(char, column, row):
            self.log.log_to_file(self.__players[self.__next_char] + ' won!')
            return True

        if self.__check_full():
            self.log.log_to_file('Nobody won!')
            return True

        return False

    def __check_lines(self, char, column, row):
        return self.__check_column(char, column) or self.__check_row(char, row)

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
        return self.__cell_counter == 0
