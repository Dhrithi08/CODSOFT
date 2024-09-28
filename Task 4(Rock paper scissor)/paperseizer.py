import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        self.root.config(bg="#e0f7fa")
        
        # Variables to track scores
        self.user_score = 0
        self.computer_score = 0
        
        # Heading
        self.heading = tk.Label(self.root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#333")
        self.heading.pack(pady=10)
        
        # Display user and computer score
        self.score_label = tk.Label(self.root, text=f"User: {self.user_score} | Computer: {self.computer_score}", font=("Arial", 14), bg="#e0f7fa")
        self.score_label.pack(pady=10)

        # Label to show results
        self.result_label = tk.Label(self.root, text="Make your choice!", font=("Arial", 16), bg="#e0f7fa")
        self.result_label.pack(pady=20)

        # Buttons for Rock, Paper, Scissors
        self.create_choice_buttons()

        # Play Again Button
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game, font=("Arial", 12), bg="#4caf50", fg="white")
        self.play_again_button.pack(pady=10)
        
        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game, font=("Arial", 12), bg="#f44336", fg="white")
        self.exit_button.pack(pady=5)
    
    def create_choice_buttons(self):
        """Create buttons for the user to choose Rock, Paper, or Scissors."""
        self.button_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.button_frame.pack(pady=10)
        
        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.user_choice("Rock"), font=("Arial", 12), bg="#9e9e9e", fg="white")
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.user_choice("Paper"), font=("Arial", 12), bg="#2196f3", fg="white")
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.user_choice("Scissors"), font=("Arial", 12), bg="#f44336", fg="white")
        self.scissors_button.grid(row=0, column=2, padx=10)
    
    def user_choice(self, choice):
        """Handle user's choice and determine the winner."""
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        result = self.determine_winner(choice, computer_choice)
        
        self.result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")
        self.update_scores(result)
    
    def determine_winner(self, user, computer):
        """Determine the winner based on user and computer choices."""
        if user == computer:
            return "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            return "You win!"
        else:
            return "You lose!"
    
    def update_scores(self, result):
        """Update scores based on the result."""
        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1
        
        # Update the score display
        self.score_label.config(text=f"User: {self.user_score} | Computer: {self.computer_score}")
    
    def reset_game(self):
        """Reset the game to allow the user to play another round."""
        self.result_label.config(text="Make your choice!")
    
    def exit_game(self):
        """Exit the game and close the application."""
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
