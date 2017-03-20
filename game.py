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
        self.name = self.name_prompt()
        self.symbol = ""

    def name_prompt(self):
        if self.__name__ == "player_one":
            name = input("Please choose player 1 name (Default: Player 1): ")
            if name == "":
                return "Player 1"
        else:
            name = input("Please choose player 2 name (Default: Player 2): ")
            if name == "":
                return "Player 2"        
        return name

    def symbol_prompt(self):
        prompt_text = "{0} will go first; would you like to be 'x' or 'o'?: ".format(self.name)
        self.symbol = input(prompt_text).lower()
            while self.symbol not in ['o', 'x']:
                symbol_error = "Symbol not valid, please enter a valid symbol ('x' or 'o'): "
                self.symbol = input(symbol_error)).lower()


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
            self.player_one.symbol_prompt()
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
            firstplayer = (self.player_one.name, self.player_one.symbol)
            print("{0} will go second; your symbol is {1}".format(firstplayer[0], firstplayer[1]))
            print("{0} is {1}".format(self.player_two.name, self.player_two.symbol))

    def ask_move(self):
        """Asks for the move row, column, and then returns them"""
        row_prompt = "Please choose row 1(top), 2(middle) or 3(bottom) for your move: "
        move_row = int(input(row_prompt))
        while move_row not in range(1, 4):
            row_prompt = "Please provide legal row (1 (top), 2 (middle), 3 (bottom)): "
            move_row = int(input(row_prompt))

        col_prompt = "Please choose column 1(left), 2(middle) or 3(right) for your move: "
        move_col = int(input(col_prompt))
        while move_col not in range(1, 4):
            col_prompt = "Please choose legal column (1 (left), 2 (middle), 3 (right)): "
            move_col = int(input(col_prompt))

        move_position = ((move_row - 1) * 3) + (move_col - 1)

        if not(self.is_free(move_position)):
            error_msg = "Grid already taken; please try again with a different grid.\n"
            raise IllegalMoveError(error_msg)
        
        return move_position

    def turn(self):
        """Player takes a turn"""
        move_position = None
        if self.player_turn == 1:
            while move_position == None:
                move_position = ask_move()
            self.make_move(self.player_one.symbol, move_position)
        elif self.ai_enabled:
            #TODO: This bit
            print("Player 2 turn: \n")
            move_position = random.choice(self.available_grids)
            self.board[move_position] = self.player_two.symbol

        self.swap_player_turn()
        self.available_grids.remove(move_position)
        self.turn_num += 1
        self.draw_board()

    def game_over(self):
        game_over_msg = "Game Over; the result is a draw! Would you like to play again? Y/N: "
        answer = input(game_over_msg).upper()
        while answer is not 'Y' or 'N':
            wrong_input_msg = "Invalid input, please input yes with a 'Y' or no with an 'N': "
            answer = input(wrong_input_msg).upper()
        if answer is 'Y':
            main()
        else:
            exit(0)

def IllegalMoveError(Exception):
    pass

def main():
    """Main thread of the gaaaaaaaaaaaame"""
    __game__ = Game()  # Creates the __game__ object
    __game__.decide_symbols()
    __game__.draw_board()  # Draws the board

    while __game__.turn_num <= 9:
        __game__.turn()

main()