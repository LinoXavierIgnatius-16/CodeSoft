import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.user_label = tk.Label(master, text="User Score: 0", font=("Helvetica", 12))
        self.user_label.pack(pady=(10, 0))

        self.computer_label = tk.Label(master, text="Computer Score: 0", font=("Helvetica", 12))
        self.computer_label.pack()

        self.choices = ['rock', 'paper', 'scissors']

        for choice, color in zip(self.choices, ['red', 'blue', 'green']):
            button = tk.Button(master, text=choice.capitalize(), command=lambda c=choice: self.play_rps(c), bg=color, font=("Helvetica", 16), height=2, width=10)
            button.pack(pady=10)

    def play_rps(self, user_choice):
        computer_choice = random.choice(self.choices)
        winner = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, winner)
        self.update_scores(winner)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return 'user'
        else:
            return 'computer'

    def display_result(self, user_choice, computer_choice, winner):
        result = f"User's choice: {user_choice}\nComputer's choice: {computer_choice}\n\n"
        if winner == 'tie':
            result += "It's a tie!"
        elif winner == 'user':
            result += "You win!"
        else:
            result += "Computer wins!"
        messagebox.showinfo('Result', result)

    def update_scores(self, winner):
        self.user_score += 1 if winner == 'user' else 0
        self.computer_score += 1 if winner == 'computer' else 0
        self.user_label.config(text=f"User Score: {self.user_score}")
        self.computer_label.config(text=f"Computer Score: {self.computer_score}")

def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
