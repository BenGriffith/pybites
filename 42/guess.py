import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)
    

class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""

        user_guess = input(f"Guess a number between {START} and {END}: ")

        try:

            if isinstance(user_guess, str) and isinstance(int(user_guess), int):
                user_guess = int(user_guess)

            if user_guess == None:
                raise ValueError("Please enter a number")
            elif not isinstance(user_guess, (int, float)):
                raise ValueError("Should be a number")
            elif user_guess < 1 or user_guess > 20:
                raise ValueError("Number not in range")
            elif user_guess in self._guesses:
                raise ValueError("Already guessed")

        except ValueError:
            raise

        else:
            self._guesses.add(user_guess)
            self._validate_guess(user_guess)

        return user_guess           


    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess > self._answer:
            print(f"{guess} is too high")
        elif guess < self._answer:
            print(f"{guess} is too low")
        else:
            print(f"{guess} is correct!")
            self._win = True

        return self._win


    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < 5:
            if self._win == True:
                break
            try:
                self.guess()
            except ValueError as value_e:
                print(value_e.args[0])
        
        if self._win:
            print(f"It took you {len(self._guesses)} guesses")
        else:
            print(f"Guessed {len(self._guesses)} times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()