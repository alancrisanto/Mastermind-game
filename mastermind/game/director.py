from code_object import CodeObject
from console import Console
import random

class Director():
    """ This class is responsible for controlling the flow of gameplay
    """
    def __init__(self):
        """ The constructor method.
        ARGS: self (Director)   : an instance of Director()
        """
        self.console = Console()
        self.code = CodeObject()

        
        

    


    def start_game(self):        
        """ The method used to start the game
        ARGS: self (Director)   : an instance of Director()
        """


        code = self.code
        console = self.console
        
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

        while continue_playing:

            # player one turn

            # player two turn

            #

            # START GAME LOOP
            Player


    def player_turn(self, player):
        """
        ARGS:
            self (Director)     : an instance of Director()
            player (Player)     : an instance of Player()
        RETURNS:
            an integer
        """
        self.console.display_output(f"{player.name}'s turn:")




        self.console.display_output("")

    def validate_guess(self,guess):
        """ A method that validates whether or not a guess is within the expected range
        """
        min = self.code.min
        max = self.code.max
        if guess in range(min,(max+1)):
            return True
        else:
            return False

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

main()