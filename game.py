import random


class Game:
    def __init__(self):
        self.legal_num = [1, 2, 3]
        self.legal_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.ai_start_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.ai_enabled = False
        self.game_symbols = ['x', 'o']
        self.turn_num = 1
        self.board = [' '] * 9
        self.turn_selection = ['Player 1', 'Player 2']
        self.player_turn = None
        self.player_one_symbol = None
        self.player_two_symbol = None

    # Obviously draws the game board into the console
    def draw_board(self):
        print('\n ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' \n' +
              '---|---|---\n' +
              ' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' \n' +
              '---|---|---\n' +
              ' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' \n')

    def setup(self):


        #   def player_query(self):

    def turn(self):

        #   self.player_query()

        if self.player_turn == 'Player 1':

            # Asks the player where they would like to move
            move_row = int(raw_input("Please choose the row (1 (top), 2 (middle) or 3 (bottom)) for your move: "))
            while move_row not in self.legal_num:
                move_row = int(raw_input("Please provide a legal row value (1 (top), 2 (middle), 3 (bottom)): "))

            move_col = int(raw_input("Please choose the column (1 (left), 2 (middle) or 3 (right)) for your move: "))
            while move_col not in self.legal_num:
                move_col = int(raw_input("Please provide a legal column value (1 (left), 2 (middle), 3 (right)): "))

            move_position = ((move_row - 1) * 3) + (move_col - 1)

            while move_position not in self.legal_moves:

                print("Move was not legal, please try again with a different move.\n")

                move_row = int(raw_input("Please choose the row (1 (top), 2 (middle) or 3 (middle)) for your move: "))
                while move_row not in self.legal_num:
                    move_row = int(raw_input("Please provide a legal row value (1 (top), 2 (middle), 3 (bottom)): "))

                move_col = int(
                    raw_input("Please choose the column (1 (left), 2 (middle) or 3 (right)) for your move: "))

                while move_col not in self.legal_num:
                    move_col = int(raw_input("Please provide a legal column value (1 (left), 2 (middle), 3 (right)): "))

            move_position = ((move_row - 1) * 3) + (move_col - 1)

            self.board[move_position] = self.player_one_symbol

            self.player_turn = 'Player 2'

        else:
            print("Player 2 turn: \n")
            move_position = random.choice(self.legal_moves)
            self.board[move_position] = self.player_two_symbol
            self.player_turn = 'Player 1'

        self.legal_moves.remove(move_position)
        self.turn_num += 1

        self.draw_board()

        return


# The main thread of the game
def main():
    game = Game()  # Creates the game object
    game.draw_board()  # Draws the board
    game.player_turn = random.choice(game.turn_selection)  # Determines the player turn order
    if game.player_turn == 'Player 1':
        game.player_one_symbol = str(raw_input("Player 1 will go first; would you like to be 'x' or 'o'?: ")).lower()
        while game.player_one_symbol not in game.game_symbols:
            game.player_one_symbol = str(
                raw_input("Symbol was not valid, please enter a valid symbol ('x' or 'o'): ")).lower()
        if game.player_one_symbol is 'o':
            game.player_two_symbol = 'x'
        else:
            game.player_two_symbol = 'o'
    else:
        game.player_one_symbol = random.choice(game.game_symbols)
        if game.player_one_symbol is 'o':
            game.player_two_symbol = 'x'
        else:
            game.player_two_symbol = 'o'
        print('Player 1 will go second; your symbol is ' + game.player_one_symbol)
        print('Player 2 is ' + game.player_two_symbol)

    while game.turn_num <= 9:
        game.turn()

    answer = raw_input("Game Over; the result is a draw! Would you like to play again? Y/N: ").upper()
    while answer is not 'Y' or 'N':
        answer = raw_input("Invalid input, please input yes with a 'Y' or no with an 'N': ")
    if answer is 'Y':
        main()
    else:
        exit(0)

main()
