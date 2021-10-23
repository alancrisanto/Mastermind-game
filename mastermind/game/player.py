class Player():
    """ Responsible for storing player's name, guesses, and hints
    ATTRIBUTES:
        max_name_length (INT)   : the maxmium allowed name length
        name (STR)              : the name of the player
        last_guess (STR)        : the player's last guess
        last_hint (STR)         : the player's last hint
    """
    def __init__(self,input_name) -> None:
        """
        ARGS:
            self (Player)       : an instance of Player()
            input_name (STR)    : the name of the player
        """
        self.max_name_length = 24
        self.name = str(input_name)
        if len(self.name) > self.max_name_length:
            self.__clip_name()
        self.last_guess = '----'
        self.last_hint = '****'

    def __clip_name(self):
        """
        """
        new_name = ""
        for i in range(self.max_name_length):
            new_name += self.name[i]
        self.name = new_name