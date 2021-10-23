import random
if __name__ == "game.player":
    from game.console import Console

class Player:
    """ Responsible for storing player's name, guesses, and hints
    ATTRIBUTES:
        max_name_length (INT)   : the maxmium allowed name length
        name (STR)              : the name of the player
        last_guess (STR)        : the player's last guess
        last_hint (STR)         : the player's last hint
    """
    def __init__(self,input_name="Player") -> None:
        """
        ARGS:
            self (Player)       : an instance of Player()
            input_name (STR)    : the name of the player
        """
        self.max_name_length = 24
        self.name = str(input_name)
        if len(self.name) > self.max_name_length:
            self.clip_name()
        if self.name == "":
            self.christen_player()

        self.last_hint = '****'
        self.last_guess = '----'

    def clip_name(self):
        """ Clips self.name if it exceeds the max length
        ARGS:
            self (Player)       : an instance of Player()        
        """
        new_name = ""
        for i in range(self.max_name_length):
            new_name += self.name[i]
        self.name = new_name

    def christen_player(self):
        """ Gives a Player a new name
        ARGS:
            self (Player)       : an instance of Player()        
        """
        colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        animals = ["Cat", "Dog", "Cow", "Sparrow", "Snake", "Duck", "Spider"]
        self.name = f"{random.choice(colors)} {random.choice(animals)}"
        console = Console()
        console.display_output(f"No name huh? I hereby christen you '{self.name}.'")
        
def main():
    player = Player("Brigham Young")
    print(f"Created player with name: {player.name}")

    player = Player("Supercalifragilisticexpialidocious")
    print(f"Created player with name: {player.name}")

    player = Player()
    print(f"Created player with name: {player.name}")

    input_name = input("Enter a player name: ")
    player = Player(input_name)
    print(f"Created player with name: {player.name}")

if __name__ == "__main__":
    from console import Console
    main()