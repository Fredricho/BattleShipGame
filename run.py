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

def populate_board(board):
    while True:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ship(x, y)
            break

def play_game(player_board, computer_board):
    while True:
        print(f"{player_board.name}'s Board:")
        player_board.print_board()
        print("Computer's Board:")
        computer_board.print_board()

        while True:
            try:
                x = int(input(f"{player_board.name}, enter the row: \n "))
                y = int(input(f"{player_board.name}, enter the col: \n "))

                if not valid_coordinates(x, y, computer_board):
                    print("Invalid coordinates. Try again.")
                    continue

                result = computer_board.make_guess(x, y)
                print(result)
                if result == "Already guessed this coordinate. Try again.":
                    continue
                break
            except ValueError:
                print("Invalid input. Only integers are allowed.")

        if all(ship == "@" for ship in computer_board.ships):
            print(f"Congratulations, {player_board.name}! You found all the computer's ships!")
            break

        print("Computer is making a guess...")
        while True:
            x = random_point(player_board.size)
            y = random_point(player_board.size)

            if (x, y) not in player_board.guesses:
                result = player_board.make_guess(x, y)
                print(result)
                break

        if all(ship == "@" for ship in player_board.ships):
            print("The computer found all your ships! You lose.")
            break