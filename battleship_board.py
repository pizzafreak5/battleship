
EMPTY = 'EMPTY'
MISS = 'MISS'
SHIP = 'SHIP'
HIT = 'HIT'

class Board:

    def __init__ (self, size = 10):

        self.board = []
        self.last_change = (EMPTY, 0, 0)
        self.size = size

        for i in range(size):
            elem = []
            for i in range(size):
                elem.append(EMPTY)

            self.board.append(elem)

    def get_last_change(self):
        return self.last_change

    #This function is called to attack a square on the board
    #it returns hit or miss, and changes the board
    def attack(self, x, y):

        if x > self.size or y > self.size: #Check that coord is in bounds
            return 'OUT OF BOUNDS'

        if self.board[x][y] == SHIP:
            self.board[x][y] = HIT
            self.last_change = (HIT, x, y)
            return HIT

        elif self.board[x][y] == EMPTY:
            self.board[x][y] = MISS
            self.last_change = (MISS, x, y)
            return MISS

        else:
            return 'REPEAT'

    #This function checks the square provided.
    def check(self, x, y):

        if x > self.size or y > self.size: #Check that coord is in bounds
            return 'OUT OF BOUNDS'
        
        return self.board[x][y]

    def size(self):
        return self.size

    #Prints the board to console
    def print_board(self):

        top_string = '' # The topstring will contain the numbers for colums
        row_string = ''
        format_str = '{:<6}'

        top_string += format_str.format('')
        for i in range(self.size):
            top_string += format_str.format(str(i))

        print(top_string)

        for i in range(self.size):
            row_string += format_str.format(str(i))

            for j in range(self.size):
                row_string += format_str.format(self.board[i][j])

            print(row_string)
            row_string = ''

    
            
            

    
