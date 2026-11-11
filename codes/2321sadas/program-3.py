import tkinter as tk

root = tk.Tk()
root.title("XO Game")

board = [""] * 9

def check(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(all(board[i] == p for i in w) for w in wins)

def ai_move():
    for p in ["O", "X"]:
        for i in range(9):
            if board[i] == "":
                board[i] = p
                if check(p):
                    return i
                board[i] = ""

    for i in [4,0,2,6,8,1,3,5,7]:
        if board[i] == "":
            return i

def play(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")

        if check("X"):
            result.config(text="You Win!")
            return

        if "" not in board:
            result.config(text="Draw!")
            return

        j = ai_move()
        board[j] = "O"
        buttons[j].config(text="O", state="disabled")

        if check("O"):
            result.config(text="AI Wins!")
        elif "" not in board:
            result.config(text="Draw!")

buttons = []

for i in range(9):
    b = tk.Button(root, text="", font=("Arial", 25),
                  width=5, height=2,
                  command=lambda i=i: play(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

result = tk.Label(root, text="Human: X | AI: O",
                  font=("Arial", 15))
result.grid(row=3, column=0, columnspan=3)

root.mainloop()
