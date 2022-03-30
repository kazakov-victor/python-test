class Logger:
    @staticmethod
    def log_to_file(message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

    @staticmethod
    def show_board(board):
        for i in range(len(board)):
            str1 = ''
            for j in range(len(board[i])):
                str1 += board[j][i]

                if j < len(board) - 1:
                    str1 += '|'
            print(str1)
            if i < len(board) - 1:
                print('_ ' * len(board))
