import random

class game:
    def __init__(self):
        self.choice = ["y", "n"]
    def random_rolling(self):
      roll = random.randint(1,6)
      return roll
    def get_user_choice(self):
        while True:
            choice = input("Roll the dice? (y/n): ").lower()
            if choice == "y":
              die1 = random.randint(1,6)
              die2 = random.randint(1,6)
              print(f'{die1}, {die2}')
            elif choice == "n":
              print("Thanks for playing!")
            else:
              print("Invalid choice!")
game = game()
game.get_user_choice()
  