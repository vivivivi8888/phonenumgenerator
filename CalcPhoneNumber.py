import copy

class BaseChessPiece:
    def __init__(self, coordinate):
        '''Base class for all chess piece:
        Initialize the chess piece at coordinate
        '''
        self.x, self.y = coordinate
        self.last_position = []

    def generate_possible_moves(self):
        raise NotImplementedError('Chess piece move not implemented')

    def move(self, move):
        self.last_position.append((self.x, self.y))
        x, y = move
        self.x, self.y = self.x + x, self.y + y

    def move_back(self):
        if self.last_position:
            self.x, self.y = self.last_position.pop()
        else:
            raise ValueError('Cannot move further back!')


class Knight(BaseChessPiece):
    # def __init__(self, coordinate):
    #   super().__init__(coordinate)

    def generate_possible_moves(self):
        # This function defines what kind of chess piece it is
        return [
            (2, 1),
            (1, 2),
            (2, -1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (-2, -1),
            (-1, -2),
        ]


class CalcPhoneNumber:
    def __init__(self, board, chess_piece):
        '''Initialize the calculation with board and type of chess_piece
        '''
        self.board = copy.deepcopy(board)
        if board:
            self.n = len(board)
            self.m = len(board[0])
        else:
            raise ValueError('board is not valid')
        self.cp_class = chess_piece

    def _check_move_valid(self, move):
        x, y = move
        if self.cp.x + x >= self.n or self.cp.x + x < 0:
            return False

        if self.cp.y + y >= self.m or self.cp.y + y < 0:
            return False

        if not self.board[self.cp.x + x][self.cp.y + y].isdigit():
            return False

        return True

    def _calc_recur(self, c_number):
        # If c_number contains 7 valid digit, it becomes a phone number
        if len(c_number) == 7:
            self.total_valid_number += 1
            self.all_possible_number.append(c_number)
            return

        # Recursively go through all possible moves
        for move in self.cp.generate_possible_moves():
            if self._check_move_valid(move):
                self.cp.move(move)
                self._calc_recur(c_number + self.board[self.cp.x][self.cp.y])
                self.cp.move_back()

    def calc(self):
        # Initialize count for each calc
        self.total_valid_number = 0
        # Store all possible number for sanity check
        self.all_possible_number = []
        
        for i in range(self.n):
            for j in range(self.m):
                if (self.board[i][j].isdigit()
                    and self.board[i][j] != '0' and self.board[i][j] != '1'):
                    # Start chess piece at valid start position
                    self.cp = self.cp_class((i,j))
                    # Calculate possible phone number start from this position
                    self._calc_recur(self.board[i][j])

        ###  Sanity Check statement  ###
        print(len(self.all_possible_number))
        print(self.all_possible_number)
        
        return self.total_valid_number


if __name__ == '__main__':
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#'],
    ]
    c = CalcPhoneNumber(board, Knight)
    print(c.calc())
