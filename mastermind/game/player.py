class Player():
    """ Responsible for storing player's name, guesses, and hints
    ATTRIBUTES:
        name (STR)          : the name of the player
        last_guess (STR)    : the player's last guess
        last_hint (STR)     : the player's last hint
    """
    def __init__(self,input_name) -> None:
        """
        ARGS:
            self (Player)       : an instance of Player()
            input_name (STR)    : the name of the player
        """
        self.name = str(input_name)
        self.last_guess = '----'
        self.last_hint = '****'
    