import random

class HangmanGame:
    def __init__(self):
        self.word_lists = {
            "Fruits": ["apple", "banana", "orange", "grape", "kiwi", "peach", "strawberry", "watermelon", "pineapple", "blueberry"],
            "Countries": ["india", "usa", "china", "russia", "brazil", "japan", "germany", "france", "canada", "australia"]
        }
        self.user_name = ""
        self.difficulty_level = ""
        self.word_list = []
        self.word = ""
        self.word_state = ""
        self.incorrect_guesses = 0
        self.remaining_guesses = 0
        self.score = 0

    def select_user_profile(self):
        self.user_name = input("Enter your name: ")
        print("Welcome, {}!".format(self.user_name))
        self.select_difficulty_level()

    def select_difficulty_level(self):
        print("Select difficulty level:")
        print("1. Easy (10 guesses)")
        print("2. Medium (7 guesses)")
        print("3. Hard (5 guesses)")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            self.difficulty_level = "Easy"
            self.remaining_guesses = 10
        elif choice == "2":
            self.difficulty_level = "Medium"
            self.remaining_guesses = 7
        elif choice == "3":
            self.difficulty_level = "Hard"
            self.remaining_guesses = 5
        else:
            print("Invalid choice. Defaulting to Easy difficulty.")
            self.difficulty_level = "Easy"
            self.remaining_guesses = 10

    def select_word_list(self):
        print("Select word list:")
        print("1. Fruits")
        print("2. Countries")
        print("3. Custom")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            self.word_list = self.word_lists["Fruits"]
        elif choice == "2":
            self.word_list = self.word_lists["Countries"]
        elif choice == "3":
            custom_list = input("Enter your custom word list (comma-separated): ")
            self.word_list = custom_list.split(",")
        else:
            print("Invalid choice. Defaulting to Fruits word list.")
            self.word_list = self.word_lists["Fruits"]

    def select_random_word(self):
        self.word = random.choice(self.word_list)
        self.word_state = "_" * len(self.word)

    def display_hangman(self):
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
            """,
            """
               --------
               |      |
               |      O
               |     
               |      
               |     
            """,
            """
               --------
               |      |
               |      
               |     
               |      
               |     
            """
        ]
        return stages[self.incorrect_guesses]

    def initialize_word_state(self):
        self.word_state = "_" * len(self.word)

    def update_word_state(self, letter):
        updated_state = ""
        for i in range(len(self.word)):
            if self.word[i] == letter:
                updated_state += letter
            else:
                updated_state += self.word_state[i]
        self.word_state = updated_state

    def is_game_won(self):
        return "_" not in self.word_state

    def play(self):
        self.select_user_profile()
        self.select_word_list()
        self.select_random_word()
        self.initialize_word_state()

        print("Welcome to Hangman, {}!".format(self.user_name))
        print("Difficulty Level: {}".format(self.difficulty_level))
        print("Word:", self.word_state)

        while self.incorrect_guesses < len(self.display_hangman()) - 1:
            print("Remaining guesses:", self.remaining_guesses)
            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in self.word:
                self.update_word_state(guess)
                print("Correct!")
            else:
                self.incorrect_guesses += 1
                self.remaining_guesses -= 1
                print("Incorrect guess.")
                print(self.display_hangman())

            print("Word:", self.word_state)

            if self.is_game_won():
                print("Congratulations, {}! You guessed the word: {}".format(self.user_name, self.word))
                break

        if not self.is_game_won():
            print("Sorry, {}! You ran out of guesses. The word was: {}".format(self.user_name, self.word))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset()
            self.play()
        else:
            print("Thanks for playing, {}!".format(self.user_name))

    def reset(self):
        self.word = ""
        self.word_state = ""
        self.incorrect_guesses = 0
        self.remaining_guesses = 0

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
