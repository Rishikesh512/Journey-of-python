import random

class GuessGame:
    def __init__(self):
        self.number = random.randint(1, 50)
        self.attempts = 0

    def play(self):
        while True:
            guess = int(input("Enter your guess: "))
            self.attempts += 1

            if guess > self.number:
                print("Too high")
            elif guess < self.number:
                print("Too low")
            else:
                print("Correct!")
                print("Attempts:", self.attempts)
                break


game = GuessGame()
game.play()
