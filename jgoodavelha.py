import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.board = [" " for x in range(9)]
        self.turn = "X"
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master, text=" ", font=("Helvetica", 32), height=2, width=4, command=lambda x=i, y=j: self.make_move(x, y))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def make_move(self, x, y):
        button = self.buttons[x * 3 + y]
        if button["text"] == " ":
            button["text"] = self.turn
            self.board[x * 3 + y] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"
        if self.is_victory(self.turn):
            for button in self.buttons:
                button["state"] = "disabled"
            self.display_message("{} GANHOUUUU!".format(self.turn))
        elif self.is_draw():
            for button in self.buttons:
                button["state"] = "disabled"
            self.display_message("EMPATE!!!!")

    def display_message(self, message):
        label = tk.Label(text=message, font=("Helvetica", 32))
        label.grid(row=3, column=0, columnspan=3)

    def is_victory(self, icon):
        if (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon) or \
           (self.board[3] == icon and self.board[4] == icon and self.board[5] == icon) or \
           (self.board[6] == icon and self.board[7] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[3] == icon and self.board[6] == icon) or \
           (self.board[1] == icon and self.board[4] == icon and self.board[7] == icon) or \
           (self.board[2] == icon and self.board[5] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[4] == icon and self.board[8] == icon) or \
           (self.board[2] == icon and self.board[4] == icon and self.board[6] == icon):
            return True
        else:
            return False

    def is_draw(self):
        if " " not in self.board:
            return True
        else:
           return False

root = tk.Tk()
root.title("JOGO DA VELHA")
game = TicTacToe(root)
root.mainloop()
