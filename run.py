from random import randint

class GameBoard():
    def __init__(self, size, num_of_ships, name, type):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]
        self.num_of_ships = num_of_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for row in self.board:
            print("  ".join(row))

    def make_guess(self, x, y):
        if (x, y) in self.guesses:
            return "Already guessed this coordinate. Try again."

        self.guesses.append((x, y))

        if (x, y) in self.ships:
            self.board[x][y] = "@"
            return "Hit"
        else:
            self.board[x][y] = "X"
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_of_ships:
            print("You cannot add any more ships")
        else:
            self.ships.append((x, y))

def random_point(size):
    return randint(0, size - 1)

def valid_coordinates(x, y, board):
    if x < 0 or y < 0 or x >= board.size or y >= board.size:
        return False
    return True