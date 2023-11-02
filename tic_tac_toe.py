from tkinter import messagebox, Tk, Button, Entry, Label, StringVar

class TicTacToe:
    def __init__(self, root):
        # Initialize the game window
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x400")
        self.root.configure(bg="#3498db")
        self.player1_name = StringVar()
        self.player2_name = StringVar()

        # Create and place labels and entry widgets for player names
        player1_label = Label(root, text="Player 1 (X):", font=("Arial", 14), bg="#3498db", fg="white")
        player1_label.grid(row=0, column=0, padx=10, pady=(50, 5))
        player1_entry = Entry(root, textvariable=self.player1_name, font=("Arial", 14))
        player1_entry.grid(row=0, column=1, padx=10, pady=(50, 5))

        player2_label = Label(root, text="Player 2 (O):", font=("Arial", 14), bg="#3498db", fg="white")
        player2_label.grid(row=1, column=0, padx=10, pady=5)
        player2_entry = Entry(root, textvariable=self.player2_name, font=("Arial", 14))
        player2_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create and place the "Start Game" button
        start_button = Button(root, text="Start Game", font=("Arial", 14), command=self.start_game, bg="#2ecc71", fg="white")
        start_button.grid(row=2, columnspan=2, pady=20)

        # Initialize the buttons grid
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

    def start_game(self):
        # Start the game by creating and placing the buttons for the Tic-Tac-Toe grid
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.root, text="", font=("Arial", 24, "bold"), width=5, height=2,
                                           command=lambda row=i, col=j: self.on_click(row, col), bg="#ecf0f1")
                self.buttons[i][j].grid(row=i + 3, column=j, padx=5, pady=5)

    def on_click(self, row, col):
        # Handle button clicks during the game
        if self.buttons[row][col]["text"] == "" and not self.check_winner():
            self.buttons[row][col]["text"] = self.current_player
            if self.check_winner():
                winner = self.player1_name.get() if self.current_player == "X" else self.player2_name.get()
                messagebox.showinfo("Winner!", f"Player {winner} wins!")
            else:
                self.toggle_player()

    def toggle_player(self):
        # Switch the current player
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check if there is a winner
        # Check rows
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
        # Check columns
        for j in range(3):
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                return True
        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "" or \
           self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

if __name__ == "__main__":
    # Run the game when the script is executed
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()
