import unittest
import game

full_board = [['x', 'o', 'o'], ['o', 'x', 'o'], ['x', 'x', 'x']]
win_100_column = [['o', 'o', 'o'], [' ', ' ', ' '], [' ', ' ', ' ']]
win_010_column = [[' ', ' ', ' '], ['o', 'o', 'o'], [' ', ' ', ' ']]
win_001_column = [[' ', ' ', ' '], [' ', ' ', ' '], ['o', 'o', 'o']]
win_200_column = [['x', 'x', 'x'], [' ', ' ', ' '], [' ', ' ', ' ']]
win_020_column = [[' ', ' ', ' '], ['x', 'x', 'x'], [' ', ' ', ' ']]
win_002_column = [[' ', ' ', ' '], [' ', ' ', ' '], ['x', 'x', 'x']]
win_100_row = [['x', ' ', ' '], ['x', ' ', ' '], ['x', ' ', ' ']]
win_010_row = [[' ', 'x', ' '], [' ', 'x', ' '], [' ', 'x', ' ']]
win_001_row = [[' ', ' ', 'x'], [' ', ' ', 'x'], [' ', ' ', 'x']]
win_1_diagonal = [['x', ' ', ' '], [' ', 'x', ' '], [' ', ' ', 'x']]
win_2_diagonal = [[' ', ' ', 'x'], [' ', 'x', ' '], ['x', ' ', ' ']]


class TestStringMethods(unittest.TestCase):
    def test_is_full(self):
        game.board = full_board
        self.assertTrue(game.is_game_over())

    def test_100_column(self):
        game.board = win_100_column
        self.true_for_column()

    def test_010_column(self):
        game.board = win_010_column
        self.true_for_column()

    def test_001_column(self):
        game.board = win_001_column
        self.true_for_column()

    def test_100_row(self):
        game.board = win_100_row
        self.true_for_row()

    def test_010_row(self):
        game.board = win_010_row
        self.true_for_row()

    def test_001_row(self):
        game.board = win_001_row
        self.true_for_row()

    def test_1_diagonal(self):
        game.board = win_1_diagonal
        self.true_for_diagonal()

    def test_2_diagonal(self):
        game.board = win_2_diagonal
        self.true_for_diagonal()

    def true_for_column(self):
        self.assertTrue(game.check_lines())
        self.assertFalse(game.check_full())
        self.assertFalse(game.check_diagonals())
        self.assertTrue(game.is_game_over())

    def true_for_row(self):
        self.assertTrue(game.check_lines())
        self.assertFalse(game.check_full())
        self.assertFalse(game.check_diagonals())
        self.assertTrue(game.is_game_over())

    def true_for_diagonal(self):
        self.assertFalse(game.check_lines())
        self.assertFalse(game.check_full())
        self.assertTrue(game.check_diagonals())
        self.assertTrue(game.is_game_over())
