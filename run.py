"""
Import randint from random
"""
from random import randint
# This class is inlfuenced by the CI scoping video.
class GameBoard():
    """
    GameBoard is the the class, that sets the size, number of ships, name, type (if player or computer),
    . Has the methods of printing the board and also add ships and guesses.
    """
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
            self.ships.remove((x, y))  
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
    """
    Function to return a random coordinate between 0 and the given size of the board
    """
    return randint(0, size - 1)

def valid_coordinates(x, y, board):
    """
    Check if the given coordinate is valid for the board's range
    """
    if x < 0 or y < 0 or x >= board.size or y >= board.size:
        return False
    return True

def populate_board(board):
    """
    The function for placing out the correc amount of ships
    """
    while True:
        x = random_point(board.size)
        y = random_point(board.size)
        if (x, y) not in board.ships:
            board.add_ship(x, y)
            break

def play_game(player_board, computer_board):
    """
    This function handles the guesses, validation and checks if all of the ships were found.
    """
    while True:
        print(f"{player_board.name}'s Board:")
        player_board.print_board()
        print("Computer's Board:")
        computer_board.print_board()

        while True:
            try:
                x = int(input(f"{player_board.name}, enter the row, Integers: 0 -4: \n "))
                y = int(input(f"{player_board.name}, enter the col Intergers: 0-4 : \n "))

                if not valid_coordinates(x, y, computer_board):
                    print("Invalid coordinates. Guess at a integer from 0 - 4")
                    continue

                result = computer_board.make_guess(x, y)
                print(result)
                if result == "Already guessed this coordinate. Try again.":
                    continue
                break
            except ValueError:
                print("Invalid input. Only integers are allowed.")

        if len(computer_board.ships) == 0:
            print(f"Congratulations, {player_board.name}! You found all the computer's ships!")
            return "win"

        print("Computer is making a guess...")
        while True:
            x = random_point(player_board.size)
            y = random_point(player_board.size)

            if (x, y) not in player_board.guesses:
                result = player_board.make_guess(x, y)
                print(result)
                break

        if len(player_board.ships) == 0:
            print("The computer found all your ships! You lose.")
            return "Loose"

def run_game():
    """
    This is the function that runs the game, sets the size and num of ships, validates
    the username and asks for a rematch
    """
    size = 5
    num_of_ships = 4

    print("-" * 35)
    print("Welcome to Battleship Game \n")
    print("Guess and shoot at the enemy's board")
    print("The first to destroy all of the enemy's ships wins. \n")
    print(f"Board size: {size}. Number of ships: {num_of_ships}")
    print("Top left corner is row: 0 col: 0 \n")

    while True:
        username = input("Enter your name: \n ")
        if username.isalpha():
            break
        else:
            print("Invalid name. Only letters are allowed.")


    while True:
        computer_board = GameBoard(size, num_of_ships, "computer", type="computer")
        player_board = GameBoard(size, num_of_ships, username, type="player")

        for _ in range(num_of_ships):
            populate_board(player_board)
            populate_board(computer_board)

        result = play_game(player_board, computer_board)


        print(f"{player_board.name}'s Board after the last hit:")
        player_board.print_board()
        print("Computer's Board after the last hit:")
        computer_board.print_board()

        print(f"{player_board.name} {result} the game!")


        while True:
            play_again = input("Do you want to play again? (yes/no) \n ")
            if play_again.lower() == "yes":
                break
            elif play_again.lower() == "no":
                print("Thank you for playing! Goodbye!")
                return
            else:
                print("Invalid input. Please answer with either 'yes' or 'no'.")

    

run_game()