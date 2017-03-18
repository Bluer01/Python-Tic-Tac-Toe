"""This is where the __game__ main logic is kept"""
import random

#TODO: Add lose conditions
#TODO: See if you can clean up the decide_symbols function more
#TODO: Make the turn work better for player orders (Idea: players[abs([turn_num-1]))
#TODO: Decide whether to make the board and players global or inside the game class
#TODO: Should I even HAVE a game class?

class Player:
    """Handles the player info"""
    def __init__(self):
        self.name = ""
        self.symbol = ""

class Game:
    """This handles the board and __game__ logic"""
    def __init__(self):
        self.available_grids = [True for i in range(0, 9)]
        self.turn_num = 1
        self.player_turn = random.choice([1, 2])
        self.board = [' ' for i in range(0, 9)]
        self.ai_enabled = self.ai_prompt()
        self.player_one, self.player_two = Player(), Player()
        self.players = (self.player_one, self.player_two)

    def draw_board(self):
        """Prints the __game__ board into the console"""
        print('\n ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' \n' +
              '---|---|---\n' +
              ' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' \n' +
              '---|---|---\n' +
              ' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' \n')

    def is_free(self, chosen_x, chosen_y):
        __move_position__ = ((chosen_x - 1) * 3) + (chosen_y - 1)
        if self.available_grids[__move_position__]:
            return True
        return False

    def ai_prompt(self):
        """Asks the user if they want to player against AI"""
        while True:
            ai_answer = input("Would you like to play against the computer? (y/n): ").lower()
            if ai_answer in ('y', 'yes', 'True', '1'):
                return True
            elif ai_answer in ('n', 'no', 'False', '0'):
                return False

    def swap_player_turn(self):
        self.player_turn = abs(self.player_turn - 3)

    def make_move(self, symbol, move):
        self.board[move_position] = self.player_one.symbol

    def decide_symbols(self):
        """Determines the player turn order"""

        if self.player_turn == 1:
            self.player_one.symbol = str(input(
                "Player 1 will go first; would you like to be 'x' or 'o'?: ")).lower()
            while self.player_one.symbol not in ['o', 'x']:
                self.player_one.symbol = str(
                    input("Symbol not valid, please enter a valid symbol ('x' or 'o'): ")).lower()
            if self.player_one.symbol is 'o':
                self.player_two.symbol = 'x'
            else:
                self.player_two.symbol = 'o'
        else:
            self.player_one.symbol = random.choice(['o', 'x'])
            if self.player_one.symbol is 'o':
                self.player_two.symbol = 'x'
            else:
                self.player_two.symbol = 'o'
            print('Player 1 will go second; your symbol is ' + self.player_one.symbol)
            print('Player 2 is ' + self.player_two.symbol)

    def turn(self):
        """Player takes a turn"""
        #   self.player_query()
        move_position = None
        if self.player_turn == 1:
            while True:
                # Asks the player where they would like to move
                row_prompt = "Please choose row 1 (top), 2 (middle) or 3 (bottom) for your move: "
                move_row = int(input(row_prompt))
                while move_row not in range(1, 4):
                    row_prompt = "Please provide a legal row value (1 (top), 2 (middle), 3 (bottom)): "
                    move_row = int(input(row_prompt))

                col_prompt = "Please choose column 1 (left), 2 (middle) or 3 (right) for your move: "
                move_col = int(input(col_prompt))
                while move_col not in range(1, 4):
                    col_prompt = "Please choose a legal column (1 (left), 2 (middle), 3 (right)): "
                    move_col = int(input(col_prompt))

                move_position = ((move_row - 1) * 3) + (move_col - 1)

                while not(self.is_free(move_position)):
                    error_message = "Grid already taken; please try again with a different grid.\n"
                    raise IllegalMoveError(error_message)
                
                break
            assert move_position != None
            self.make_move(self.player_one.symbol, move_position)

            self.swap_player_turn()

        else:
            print("Player 2 turn: \n")
            move_position = random.choice(self.is_legal)
            self.board[move_position] = self.player_two.symbol
            self.swap_player_turn()

        self.is_legal.remove(move_position)
        self.turn_num += 1

        self.draw_board()

        return


def IllegalMoveError(Exception):
    pass

def main():
    """Main thread of the gaaaaaaaaaaaame"""
    __game__ = Game()  # Creates the __game__ object
    __game__.decide_symbols()
    __game__.draw_board()  # Draws the board

    while __game__.turn_num <= 9:
        __game__.turn()

    answer = input(
        "__game__ Over; the result is a draw! Would you like to play again? Y/N: ").upper()
    while answer is not 'Y' or 'N':
        answer = input(
            "Invalid input, please input yes with a 'Y' or no with an 'N': ")
    if answer is 'Y':
        main()
    else:
        exit(0)

main()