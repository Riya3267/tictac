class TicTacToe:

    def __init__(self):
        # Create board with 9 empty spaces
        self.board = [" " for _ in range(9)]

        # First player
        self.current_player = "X"

    # Display board
    def show_board(self):

        print()
        print(self.board[0], "|", self.board[1], "|", self.board[2])
        print("--|---|--")
        print(self.board[3], "|", self.board[4], "|", self.board[5])
        print("--|---|--")
        print(self.board[6], "|", self.board[7], "|", self.board[8])
        print()

    # Check winner
    def check_winner(self):

        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for condition in win_conditions:

            a, b, c = condition

            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True

        return False

    # Check draw
    def check_draw(self):

        return " " not in self.board

    # Switch player
    def switch_player(self):

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    # Main game function
    def play_game(self):

        while True:

            self.show_board()

            # Safe input
            try:
                position = int(
                    input(f"Player {self.current_player}, enter position (1-9): ")
                ) - 1

                # Check valid range
                if position < 0 or position > 8:
                    print("Invalid position! Enter between 1 and 9.")
                    continue

            except ValueError:
                print("Please enter only numbers!")
                continue

            # Check empty position
            if self.board[position] == " ":
                self.board[position] = self.current_player
            else:
                print("Position already taken!")
                continue

            # Check winner
            if self.check_winner():
                self.show_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check draw
            if self.check_draw():
                self.show_board()
                print("Game Draw!")
                break

            # Change player
            self.switch_player()


# Create object
game = TicTacToe()

# Start game
game.play_game()