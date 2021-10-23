from game.code_object import CodeObject
from game.console import Console
from game.ascii_art import AsciiArt
######
from game.temp_a import Arbiter # update with Felix's code
from game.player import Player
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
        self.arbiter = Arbiter()
        self.art = AsciiArt()

        self.continue_playing = True

    class InvalidPlayerCount(Exception):
        """ Raised when player number is not valid
        """
        pass
       
    def start_game(self):        
        """ The method contains the entire game loop from start to end
        ARGS:
            self (Director)     : an instance of Director()
            player_count (INT)  : an instance
        """
        # define variables
        code = self.code.secret_code
        console = self.console
        arbiter = self.arbiter
        art = self.art

        continue_playing = self.continue_playing

        # start_game() only
        default_player_count = 2
        player_list = []

        # start
        self.start_banner()

        # make sure player count is valid
        player_count = console.take_input("How many players are playing? (1-10) ")

        if player_count == "":
                console.display_output(f"Defaulting to {default_player_count} players")
                player_count = default_player_count
        else:        
            try:
                player_count = int(player_count)
                self.check_player_count(player_count)

            except (ValueError, self.InvalidPlayerCount):
                console.display_output(f"Invalid input \"{player_count}\"")
                console.display_output(f"Defaulting to {default_player_count} players.")
                player_count = default_player_count

        console.display_output(f"\nStarting a {player_count}-player game.\n")

        # Create Player() objects
        for i in range(1,player_count+1):
            player_name = console.take_input(f"Enter a name for Player {i}: ")

            PlayerObject = Player(player_name)
            player_list.append(PlayerObject)

        # TEST CODE
        # remove before submitting
        test = True             
        if test:
            code = 1234
        
        # start gameplay
        while continue_playing:            

            for player in player_list:

                # take player's guess
                guess = self.player_turn(player)

                # check for victory
                if guess == code:
                    continue_playing = False
                    self.victory_for(player)
                    break

                # arbiter compares Player's guess and updates hint
                player.last_hint = arbiter.check_guess(code,guess)

                # display all hints
                self.display_hints(player_list)

        art.game_over()

    def check_player_count(self,input):
        """ Checks if player_count is valid
        """
        try:
            player_count = int(input)
            if player_count >= 1 and player_count <= 10:
                pass
            else:
                raise self.InvalidPlayerCount

        except ValueError:
            raise self.InvalidPlayerCount

        
    class InvalidGuess(Exception):
        """ Error when the guess is not a valid guess
        """
        pass

    def start_banner(self):
        """ Displays a banner at the start of the game
        """
        console = self.console
        console.display_output("="*48)
        console.display_output('{:1}{:^46s}{:1}'.format("|","MASTERMIND","|"))
        console.display_output("="*48)

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
            except self.InvalidGuess:
                console.display_output("Invalid input.")
                continue

            if is_valid_guess == True:
                break
            else:
                continue
        
        # record player's last guess
        player.last_guess = guess
        
        return guess

    def display_hints(self, player_list):
        """ 
        ARGS:
            self (Director)     : an instance of Director()
            player_list (LIST)  : the list of Player() Objects
        RETURNS:
            a guess (INT)
        """
        console = self.console
        
        console.display_output("-" * 48)
        for player in player_list:
            console.display_output('{:28}{:10}{:10}'.format(f"Player {player.name}: ",f"{player.last_guess}",f"{player.last_hint}"))
            #console.display_output(f"Player {player.name}: {player.last_guess}, {player.last_hint}")
        console.display_output("-" * 48)
            
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

    def victory_for(self, player):
        """Execute if a player is victorious
        ARGS:
            self (Director)     : an instance of Director()
            player (Player)     : an instance of Player()        
        """
        console = self.console
        console.display_output(f"{player.name} won!")

    def validate_guess(self,guess):
        """ A method that validates whether or not a guess is within the expected range
        """
        min = self.code.min
        max = self.code.max
        if guess >= min and guess <= max:
            return True
        else:
            raise self.InvalidGuess

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