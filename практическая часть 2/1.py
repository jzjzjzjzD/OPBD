import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Крестики-нолики бера")

buttons = []
current_player = "X"
def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        check_winner(current_player)
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
def check_winner(player):
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player:
            messagebox.showinfo("Победа!", f"Игрок {player} победил!")
            reset_game()
            return
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player:
            messagebox.showinfo("Победа!", f"Игрок {player} победил!")
            reset_game()
            return
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:
        messagebox.showinfo("Победа!", f"Игрок {player} победил!")
        reset_game()
        return
    if buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] == player:
        messagebox.showinfo("Победа!", f"Игрок {player} победил!")
        reset_game()
        return
    is_tie = True
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                is_tie = False
                break
    if is_tie:
        messagebox.showinfo("Ничья!", "Ничья!")
        reset_game()
def reset_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                           command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

root.mainloop()
