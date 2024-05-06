import random

class UserProfile:
    def __init__(self, name, avatar, preferred_difficulty="medium"):
        self.name = name
        self.avatar = avatar
        self.preferred_difficulty = preferred_difficulty
        self.win_count = 0
        self.loss_count = 0
        self.tie_count = 0

class RockPaperScissorsGame:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.difficulty_levels = {"easy": 0, "medium": 1, "hard": 2}
        self.user_choice = ""
        self.computer_choice = ""
        self.result = ""

    def create_user_profile(self):
        name = input("Enter your name: ")
        avatar = input("Enter your avatar name: ")
        self.users[name] = UserProfile(name, avatar)
        print("User profile created successfully!")

    def select_user_profile(self):
        name = input("Enter your name to select profile: ")
        if name in self.users:
            self.current_user = self.users[name]
            print("Welcome back, {}!".format(name))
        else:
            print("User profile not found. Creating new profile.")
            self.create_user_profile()
            self.current_user = self.users[name]

    def get_user_choice(self):
        while True:
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            if user_choice in ["rock", "paper", "scissors"]:
                return user_choice
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "win"
        else:
            return "lose"

    def display_result(self):
        print("\n{} chose: {}".format(self.current_user.name, self.user_choice))
        print("The computer chose: {}".format(self.computer_choice))
        print("Result: {}".format(self.result))

    def track_scores(self):
        if self.result == "win":
            self.current_user.win_count += 1
        elif self.result == "lose":
            self.current_user.loss_count += 1
        else:
            self.current_user.tie_count += 1

    def display_scores(self):
        print("\n{}'s Stats - Wins: {}, Losses: {}, Ties: {}".format(self.current_user.name,
                                                                      self.current_user.win_count,
                                                                      self.current_user.loss_count,
                                                                      self.current_user.tie_count))

    def update_difficulty_level(self):
        difficulty = input("Select difficulty level (easy, medium, hard): ").lower()
        if difficulty in self.difficulty_levels:
            self.current_user.preferred_difficulty = difficulty
        else:
            print("Invalid difficulty level. Setting to medium.")

    def play(self):
        print("\nWelcome to Rock, Paper, Scissors!")

        while True:
            self.select_user_profile()
            self.user_choice = self.get_user_choice()
            self.computer_choice = self.get_computer_choice()
            self.result = self.determine_winner(self.user_choice, self.computer_choice)
            self.display_result()
            self.track_scores()
            self.display_scores()

            self.update_difficulty_level()

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing, {}!".format(self.current_user.name))
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
