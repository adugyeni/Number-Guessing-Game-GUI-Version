import random
import tkinter as tk
from tkinter import messagebox


# Original Game Logic
def guess_the_number_game_console(guess, target, attempts, max_attempts):
    attempts += 1
    if guess < target:
        msg = f"Too low! Try again. ({max_attempts - attempts} attempts left)"
        finished = False
        color = "red"
    elif guess > target:
        msg = f"Too high! Try again. ({max_attempts - attempts} attempts left)"
        finished = False
        color = "red"
    else:
        msg = f"Yay! You guessed it in {attempts} attempts."
        finished = True
        color = "green"
    return msg, attempts, finished, color


# GUI
class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Number Guessing Game")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e2f")

        # Game Variables
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5

        # Fonts
        self.title_font = ("Helvetica", 16, "bold")
        self.normal_font = ("Helvetica", 12)
        self.feedback_font = ("Helvetica", 14, "bold")

        # Title
        self.title_label = tk.Label(root, text="🎯 Guess the Number!", font=self.title_font, fg="white", bg="#1e1e2f")
        self.title_label.pack(pady=15)

        # Instructions
        self.instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.\nCan you guess it?", font=self.normal_font, fg="white", bg="#1e1e2f")
        self.instruction_label.pack()

        # Attempts Display
        self.attempts_label = tk.Label(root, text=f"Attempts Left: {self.max_attempts}", font=self.normal_font, fg="white", bg="#1e1e2f")
        self.attempts_label.pack(pady=10)

        # Input Entry
        self.input_entry = tk.Entry(root, font=self.normal_font, justify="center")
        self.input_entry.pack(pady=10)
        self.input_entry.focus()

        # Submit Button
        self.submit_button = tk.Button(root, text="Submit Guess", font=self.normal_font, command=self.submit_guess, bg="#4caf50", fg="white", width=15)
        self.submit_button.pack(pady=5)

        # Feedback Label
        self.feedback_label = tk.Label(root, text="", font=self.feedback_font, bg="#1e1e2f")
        self.feedback_label.pack(pady=15)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart Game", font=self.normal_font, command=self.restart_game, bg="#f44336", fg="white", width=15)
        self.restart_button.pack(pady=5)

    # Submit Guess
    def submit_guess(self):
        try:
            guess = int(self.input_entry.get())
            msg, self.attempts, finished, color = guess_the_number_game_console(guess, self.target, self.attempts, self.max_attempts)
            self.feedback_label.config(text=msg, fg=color)
            self.input_entry.delete(0, tk.END)
            self.attempts_label.config(text=f"Attempts Left: {self.max_attempts - self.attempts}")

            if finished:
                self.feedback_label.config(fg="green")
                messagebox.showinfo("Congratulations!", msg)
                self.end_game()
            elif self.attempts >= self.max_attempts:
                self.feedback_label.config(fg="red")
                messagebox.showinfo("Game Over", f"Game over! The number was {self.target}.")
                self.end_game()
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            self.input_entry.delete(0, tk.END)

    # End Game
    def end_game(self):
        self.input_entry.config(state="disabled")
        self.submit_button.config(state="disabled")

    # Restart Game
    def restart_game(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.input_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.feedback_label.config(text="")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.attempts_label.config(text=f"Attempts Left: {self.max_attempts}")

# Run the Game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGameGUI(root)
    root.mainloop()
