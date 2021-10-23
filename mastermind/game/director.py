from game.code_object import CodeObject
from game.console import Console
from game.ascii_art import AsciiArt
from game.arbiter import Arbiter
from game.player import Player
from game.player_count import PlayerCount

print(__name__)

class Director():
    """ This class is responsible for controlling the flow of gameplay
    """
    def __init__(self):
        """ The constructor method for the Director() class.
        ARGS: self (Director)   : an instance of Director()
        """
        self.console = Console()
        self.code = CodeObject()
        self.arbiter = Arbiter()
        self.art = AsciiArt()

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
        
        # start
        art.title_screen()
        self.start_banner()
        
        # Enter number of Players
        Count = PlayerCount()        
        proposed_player_count = console.take_input(f"How many players are playing? {Count.range} ")
        player_count = Count.set_player_count(proposed_player_count)
        console.display_output(Count.message) 

        # Create Player() objects
        player_list = []
        for i in range(player_count):
            player_name = console.take_input(f"Enter a name for Player {i+1}: ")
            PlayerObject = Player(player_name)
            player_list.append(PlayerObject)

        # TEST CODE
        # remove before submitting
        test = True             
        if test:
            #code = 1234
            print("code is: " + str(code))

        continue_playing = True

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
                player.last_hint = arbiter._check_guess(code,guess)

                # display art 
                art.encouragement(player.last_hint)

                # display all hints
                self.display_hints(player_list)
       
        art.game_over()

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
            # take guess                        
            try:
                guess = int(console.take_input("What is your guess? "))
            except ValueError:
                console.display_output("Invalid input.")
                continue

            # validate guess is within range
            is_valid_guess = self.validate_guess(guess)
            if not is_valid_guess:
                console.display_output("Invalid input.")

        # record player's last guess
        player.last_guess = guess
        
        return guess

    def validate_guess(self,guess):
        """ A method that validates whether or not a guess is within the expected range
        ARGS:
            self (Director)     : an instance of Director()
            guess (INT)         : the player's guess
        RETURNS:
            BOOL
        """
        min = self.code.min
        max = self.code.max
        if guess >= min and guess <= max:
            return True
        else:
            return False

    def display_hints(self, player_list):
        """ Displays the last guesses and hints for all players
        ARGS:
            self (Director)     : an instance of Director()
            player_list (LIST)  : the list of Player() Objects
        RETURNS:
            a guess (INT)
        """
        console = self.console

        console.display_output("-" * 48)
        for player in player_list:
            console.display_output('{:32}{:8}{:8}'.format(f"Player {player.name}: ",f"{player.last_guess}",f"{player.last_hint}"))
        console.display_output("-" * 48)
            
    def victory_for(self, player):
        """Execute if a player is victorious
        ARGS:
            self (Director)     : an instance of Director()
            player (Player)     : an instance of Player()        
        """
        console = self.console
        console.display_output(f"{player.name} won!")

# for testing
def main():
    print("Creating Director() instance...")
    dir = Director()
    print("Success.")

if __name__ == "__main__":
    main()