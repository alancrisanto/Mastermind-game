class PlayerCount():
    """ A class of objects responsible for checking whether
    the entered number of players is within the acceptable range.
    ATTRIBUTES:
        _default (INT)  : the default number of players
        _min (INT)      : the minimum allowed players
        _max (INT)      : the maximum allowed players
        range           : a string showing the allowed range
    """
    def __init__(self) -> None:
        """ Constructor method for the PlayerCount() class
        ARGS:
            self (PlayerCount)  : an instance of PlayerCount()
        """
        
        self.default = 2
        self.min = 1
        self.max = 10
        self.range = f"({self.min}-{self.max})"

        self.message = ""

    def set_player_count(self, player_count):
        """ Validates that the number of players entered is valid, updates the message
        ARGS:
            self (PlayerCount)  : an instance of PlayerCount()
            player_count (INT)  : the number of players
        RETURN:
            player_count (INT)
        """
        
        #1 make sure input is an integer
        
        try: 
            player_count = int(player_count)
            if player_count in range(self.min, self.max+1):
                self.message += f"Starting a {player_count}-player game\n"

            else: # input is INT but not within range
                self.message += f"Invalid input '{player_count}'\n"
                self.message += f"Defaulting to {self.default} players\n"
                player_count = self.default

        except ValueError:
            if player_count == "": # blank input
                player_count = self.default
                self.has_message = True
                self.message += (f"Defaulting to {self.default} players\n")
                player_count = self.default                
            else: # user entered non-INT non blank
                self.message += f"Invalid input '{player_count}'\n"
                self.message += f"Defaulting to {self.default} players\n"
                player_count = self.default

        return player_count