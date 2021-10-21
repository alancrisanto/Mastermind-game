from game.code_object import CodeObject
from game.console import Console
#from ascii_art import AsciiArt
from game.arbiter import Arbiter
from game.player import Player
import random

class InvalidGuess(Exception):
        """ Raise this error when the guess is not a valid guess
        """
        pass

class Director():
    """ This class is responsible for controlling the flow of gameplay
    """
    def __init__(self):
        """ The constructor method.
        ARGS: self (Director)   : an instance of Director()
        """
        self.console = Console()
        self.code = CodeObject()
        self.arbiter = Arbiter()

        # waiting
        # self.arbiter = Arbiter()
        # self.ascii_art = AsciiArt()
        
 
    def start_game(self):        
        """ The method used to start the game
        ARGS: self (Director)   : an instance of Director()
        """


        code = self.code.secret_code
        console = self.console
        # needs arbiter class
        arbiter = self.arbiter
        
        # take player names
        player_1_name = console.take_input("Enter a name for Player 1: ")
        player_2_name = console.take_input("Enter a name for Player 2: ")

        # create PlayerOne object
        self.PlayerOne = Player(player_1_name)
        p1 = self.PlayerOne
        
        # create PlayerTwo object
        self.PlayerTwo = Player(player_2_name)
        p2 = self.PlayerTwo

        # generate the code
        continue_playing = True
        
        # testing
        code = 1234
        while continue_playing:

            # player one turn
            p1_guess = self.player_turn(p1)

            # arbiter checks Player 1's guess
            hint = arbiter.check_guess(code,p1_guess)
            console.display_output(hint)

            # check victory condition
            p1_is_victorious = self.check_victory(p1)
            if p1_is_victorious:
                """# p1 victory code"""
                print('end')
                continue_playing = False
                break
            else:
                pass

            # player two turn
            p2_guess = self.player_turn(p2)

            # arbiter checks Player 2's guess
            hint = arbiter.check_guess(code,p2_guess)
            console.display_output(hint)

            p2_is_victorious = self.check_victory(p2)
            if p2_is_victorious:
                """# p2 victory code"""
                print('end')
                continue_playing = False
                break
            else:
                pass

            continue

        print('FIN.')


    def player_turn(self, player):
        """ 
        ARGS:
            self (Director)     : an instance of Director()
            player (Player)     : an instance of Player()
        RETURNS:
            a guess (INT)
        """
        console = self.console

        console.display_output(f"{player.name}'s turn:")
        is_valid_guess = False

        # guess loop
        while not is_valid_guess:
            
            try:
                guess = int(console.take_input("What is your guess? "))
            except ValueError:
                console.display_output("Invalid input.")
                continue

            try:
                is_valid_guess = self.validate_guess(guess)
            except InvalidGuess:
                console.display_output("Invalid input.")
                continue

            if is_valid_guess == True:
                break
            else:
                continue
        
        # record player's last guess

        player.last_guess = guess
        return guess
            
    def check_victory(self, player):
        """ Checks if a player's last guess was correct.
        ARGS:
        """
        code = self.code.secret_code
        guess = player.last_guess

        if code == guess:
            return True
        else:
            return False


    def validate_guess(self,guess):
        """ A method that validates whether or not a guess is within the expected range
        """
        min = self.code.min
        max = self.code.max
        if guess >= min and guess <= max:
            return True
        else:
            raise InvalidGuess

# for testing
def main():
    print("Creating Director() instance...")
    dir = Director()
    print("Success.")
    print()

    # CodeObject

    print("Creating CodeObject() instance...")
    print(f"The secret code is {dir.code.secret_code}")

    # test the validate_guess method
    test_qty = 10
    print("Testing validate_guess against CodeObject instance's min and max attributes.")
    print()
    print(f"CodeObject.min = {dir.code.min}")
    print(f"CodeObject.min = {dir.code.max}")
    print()
    

    expected_false = []

    for i in range(test_qty):
        too_small = random.randint(0,dir.code.min)
        expected_false.append(too_small)

    for i in range(test_qty):
        too_big = random.randint(dir.code.max, dir.code.max*2)
        expected_false.append(too_big)

    for number in expected_false:
        result = dir.validate_guess(number)
        if result == False:
            print(f"Testing {number}, expecting False: [OK]")
        else:
            print(f"Testing {number}, expecting False: [FAIL]")

    expected_true = []

    for i in range(test_qty):
        just_right = random.randint(dir.code.min, dir.code.max)
        expected_true.append(just_right)

    for number in expected_true:
        result = dir.validate_guess(number)
        if result == True:
            print(f"Testing {number}, expecting True: [OK]")
        else:
            print(f"Testing {number}, expecting True: [FAIL]")

if __name__ == "__main__":
    from code_object import CodeObject
    from console import Console
    main()