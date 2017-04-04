"""
This is where the game's main logic is kept. It consists of a player class and the game round class
"""
import random
import numpy
import matplotlib
import matplotlib.pyplot

#TODO: Add lose condition(s)
#TODO: See if you can clean up the decide_symbols function more
#TODO: Decide whether to make the board and players global or inside the game class
#TODO: Should I even HAVE a game class?
#TODO: Consider turning the one-line functions into lambdas

class Player:
    """
    Handles the player data and related methods

    Attributes
    ----------
    name : string
        The name that the player will be referred to as
    symbol : string
        The symbol of the player for use on the grid
    """
    def __init__(self):
        self.name = self.name_prompt()
        self.symbol = self.symbol_prompt()

    def name_prompt(self):
        """
        Asks the player(s) for the names and then returns the name.

        Returns
        -------
        name : string
            The name that the player has chosen for themselves
        """
        if self.name == "player_one":
            name = input("Please choose player 1 name (Default: Player 1): ")
            if name == "":
                return "Player 1"
        else:
            name = input("Please choose player 2 name (Default: Player 2): ")
            if name == "":
                return "Player 2"
        return name

    def symbol_prompt(self):
        """
        Asks the player(s) for the symbol(s) that they want to use for themselves
        and returns it

        Returns
        -------
        symbol : string
            The symbol that the player has chosen for themselves
        """
        prompt_text = "{0} will go first; would you like to be 'x' or 'o'?: ".format(self.name)
        symbol = input(prompt_text).lower()
        while symbol not in ['o', 'x']:
            symbol_error = "Symbol not valid, please enter a valid symbol ('x' or 'o'): "
            symbol = input(symbol_error).lower()
        return symbol

class GameRound:
    """
    This handles the board and game logic

    Attributes
    ----------
    available_grids : list of bools
        This keeps track of the available positions on the grid to make a move
    turn_num : int
        Used to keep track of the number of turns to keep track of the game length
    player_turn : int
        Used to keep track of whose turn it is
    board : list of strings
        This is the board grids which will be replaced with symbols
    ai_enabled : bool
        If this is enabled, then we know that the second player will be the AI
    player_one/two : Player
        These are the player objects used in the game round
    players : tuple of Players
        Used to store the players, which I keep to use an index over for setting the player turn
    """
    def __init__(self):
        self.available_grids = [True for i in range(0, 9)]
        self.turn_num = 1
        # First definition is random, then is later defined through player
        self.player_turn = random.choice([1, 2])
        self.board = [list(' ' for i in range(3)) for j in range(3)]
        self.ai_enabled = self.ai_enable_prompt()
        self.player_one, self.player_two = Player(), Player()
        self.players = (self.player_one, self.player_two)

    def draw_board(self):
        """Prints the game board into the console"""
        print('\n ' +
              self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2] + ' \n' +
              '---|---|---\n' + ' ' +
              self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2] + ' \n' +
              '---|---|---\n' + ' ' +
              self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2] + ' \n')

    def is_free(self, chosen_x, chosen_y):
        """Checks if a grid on the board is free"""
        __move_position__ = ((chosen_x - 1) * 3) + (chosen_y - 1)
        if self.available_grids[__move_position__]:
            return True
        return False

    def ai_enable_prompt(self):
        """Asks the user if they want to player against AI"""
        while True:
            ai_answer = input("Would you like to play against the computer? (y/n): ").lower()
            if ai_answer in ('y', 'yes', 'True', '1'):
                return True
            elif ai_answer in ('n', 'no', 'False', '0'):
                return False

    def swap_player_turn(self):
        """
        Swaps the player whose turn is next

        The logic is that since there are only 2 players, I can subtract 3 from either 1 or 2
        and it will give me the next player
        """
        self.player_turn = abs(self.player_turn - 3)

    def make_move(self, symbol, row, column):
        """Performs the chosen move on the board"""
        self.board[row][column] = symbol

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
        """
        Asks the player for their move choice (asks for row and column the combines them)
         and then returns them

        Raises
        ------
        IllegalMoveError
            If the move can't be legally made, it raises this exception

        Returns
        -------
        move_position : tuple of ints
            The row and column (respectively) used for making the move on the board
        """
        row_prompt = "Please choose row 1 (top), 2 (middle) or 3 (bottom) for your move: "
        move_row = int(input(row_prompt))
        while move_row not in range(1, 4):
            row_prompt = "Please provide legal row (1 (top), 2 (middle), 3 (bottom)): "
            move_row = int(input(row_prompt))

        col_prompt = "Please choose column 1(left), 2(middle) or 3(right) for your move: "
        move_col = int(input(col_prompt))
        while move_col not in range(1, 4):
            col_prompt = "Please choose legal column (1 (left), 2 (middle), 3 (right)): "
            move_col = int(input(col_prompt))

        move_position = (move_row-1, move_col-1)

        if not self.is_free(move_row, move_col):
            error_msg = "Grid already taken; please try again with a different grid.\n"
            raise IllegalMoveError(error_msg)
        return move_position

    def turn(self):
        """
        Contains the logic for a turn in a round. The flow can be summed like so::

            if it's the human player turn:
                ask them for their move
                make the move
            otherwise:
                simulate the AI making a choice
                make the move

            change whose turn it is
            update the available moves
            increment the turn counter
            draw the board
        """
        move_position = None
        if self.player_turn == 1:
            while move_position is None:
                move_position = self.ask_move()
            self.make_move(self.player_one.symbol, *move_position)
        elif self.ai_enabled:
            #TODO: This bit
            print("AI turn: \n")
            move_position = random.choice(self.available_grids)
            self.board[move_position[0]][move_position[1]] = self.player_two.symbol

        self.swap_player_turn()
        self.available_grids.remove(move_position)
        self.turn_num += 1
        self.draw_board()

    def restart(self):
        """
        States the result and asks the player(s) if they want to play again

        Returns
        -------
        bool
            It returns True or False based on if the player states they want to play again
        """
        #TODO: Remember to modify this when the lose conditions are in place
        game_over_msg = "Game Over; the result is a draw! Would you like to play again? Y/N: "
        answer = input(game_over_msg).upper()
        while answer not in ['Y', 'N']:
            wrong_input_msg = "Invalid input, please input yes with a 'Y' or no with an 'N': "
            answer = input(wrong_input_msg).upper()
        return True if answer is 'Y' else False

class IllegalMoveError(Exception):
    """
    Meant to be called for if a move isn't legal on the board. Merely passes, but is then dealt
    with logically where necessary
    """
    pass

def main():
    """
    The game routine

    Uses a while loop to keep looping through after each game so that it restarts automatically
    if the game ends and the player doesn't choose to quit (logically meaning that they will be
    wanting to restart it instead)::

        while True:

    Inside the loop, it creates the GameRound object for the game, then asks the players for the
    symbols and then draws the board for us to get a mental picture to decide where to move::

        game = GameRound()
        game.decide_symbols()
        game.draw_board()

    After, we then have a while loop that keeps calling for game turns until the grid is full::

        while game.turn_num <= 9:
            game.turn()

    .. note::
        This is only the situation for now until I implement the lose conditions, because with this
        we only have a draw condition for the moment, but no lose or win conditions::

    Finally, once the game is over, we have a conditional function for exiting the game, depending
    on if the player decides to restart or quit in the ''game.restart()'' function::

        if not game.restart():
            exit(0)
    """
    while True:
        game = GameRound()  # Creates the game object
        game.decide_symbols()
        game.draw_board()  # Draws the board

        while game.turn_num <= 9:
            game.turn()

        if not game.restart():
            exit(0)

if __name__ == '__main__':
    main()
