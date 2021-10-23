if __name__ == "game.director":
    from game.code_object import CodeObject
    from game.console import Console
    from game.ascii_art import AsciiArt
    from game.arbiter import Arbiter
    from game.player import Player
    from game.player_count import PlayerCount

class Director():
    """ This class is responsible for controlling the flow of gameplay
    ATTRIBUTES:
        console (Console)           : an instance of Console()
        code_object (CodeObject)    : an instance of CodeObject()
    """
    def __init__(self):
        """ The constructor method for the Director() class.
        ARGS:
            self (Director)             : an instance of Director()
        """
        self.console = Console()
      
    def start_game(self):        
        """ The method contains the entire game loop from start to end
        ARGS:
            self (Director)     : an instance of Director()
        RETURNS:
            none
        """
        # define variables       
        console = self.console
        arbiter = Arbiter()
        art = AsciiArt()
        
        # start
        art.title_screen()
        
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

        # game loop
        play_again = True
        while play_again:

            # generate code
            self.code_object = CodeObject()
            code = self.code_object.secret_code # The code to be guessed (INT)
            console.display_output("Code generated. Good luck!\n")

            # TEST CODE
            # remove before submitting
            test = True             
            if test:
                #code = 1234
                print("code is: " + str(code))

            # start gameplay
            continue_playing = True

            while continue_playing:
                for player in player_list:

                    # take player's guess
                    guess = self.player_turn(player)

                    # check for victory
                    if guess == code:
                        continue_playing = False
                        # victory
                        art.you_win(player.name)
                        break

                    # arbiter compares Player's guess and updates hint
                    player.last_hint = arbiter._check_guess(code,guess)

                    # display art 
                    art.encouragement(player.last_hint)

                    # display all hints
                    self.display_hints(player_list)

            # ask if they want to play again
            play_again = self.ask_play_again()
       
        art.game_over()
        console.display_output("Thank you for playing Mastermind!")

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
        min = self.code_object.min
        max = self.code_object.max
        if guess >= min and guess <= max:
            return True
        else:
            return False

    def display_hints(self, player_list):
        """ Displays the last guesses and hints for all players
        ARGS:
            self (Director)     : an instance of Director()
            player_list (LIST)  : a list of Player() Objects
        RETURNS:
            a guess (INT)
        """
        console = self.console

        console.display_output("-" * 48)
        for player in player_list:
            console.display_output('{:2}{:34}{:6}{:6}'.format("",f"Player {player.name}: ",f"{player.last_guess}",f"{player.last_hint}"))
        console.display_output("-" * 48)
            
    def ask_play_again(self):
        """ Ask if players want to play again
        ARGS:
            self (Director)     : an instance of Director()
        RETURNS:
            BOOL
        """
        console = self.console

        is_valid = False
        while not is_valid:
            answer = console.take_input("Do you want to play again? (y/n) ")
            if answer in ["y", "Y", "n", "N"]:
                is_valid = True
            else:
                console.display_output("Invalid input")

        if answer in ["y", "Y"]:
            return True
        else:
            return False

def main():
    print("You are running this file from the package folder.")
    print("Do not run this directly, run '__main__.py'")

if __name__ == "__main__":
    main()