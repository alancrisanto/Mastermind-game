from player import Player

class Arbiter():
    
        """Responsible for taking player's guess, checking againnst the code, returning hint
        Stereotype:
            Information Holder

        Attributes:
        _player_guesses (list): a list of strings of player's guesses
        _player_checking (list): a list to check players code
        _player_hints (list): a list of strings of player's  hints
        
        """
        def __init__(self):
            self._player_names = []
            self._player_guesses = ["----"]
            self._player_hints = ["****"]
            self.current_arbiter= ""

        def _add_names(self,names):
            for name in names:
                self._player_names.append(name.get_name())

        def _take_guess(self, player):
            pass

        
        def _player_hint(self, code, guess):
            """Creates hints based on the code and guesses given.
           
            Args:
            TBU
            """ 
            hint = ""
            for index, letter in enumerate(guess):
                if code[index] == letter:
                    hint += "x"
                elif letter in code:
                    hint += "o"
                else:
                    hint += "*"
            return hint