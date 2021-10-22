class Player:

    def __init__(self, input_name):

        """Attributes:
            _name (string): The player's name
            last_guess: the player's last guess
            last_hinte: Hint given to the player """

        self.name = str(input_name)
        self.last_guess = "----"
        self.last_hint = "****"
        self.player_gueeses = []

