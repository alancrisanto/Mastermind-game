#from player import Player

class Arbiter():
    
        """Responsible for taking player's guess, checking againnst the code, returning hint
        Stereotype:
            
        ATTRIBUTES:
            none
        """
        def __init__(self):
            pass

        def _check_guess(self, code, guess):
            """Creates hints based on the code and guesses given.
           
            Args:
                self (Arbiter)  : an instance of Arbiter
                code (INT)      : the secret code
                guess (INT)     : the player's guess
            RETURNS:
                hint (STR)
            """ 
            code = str(code)
            guess = str(guess)
            
            hint = ""
            for index, letter in enumerate(guess):

                # CORRECT number in CORRECT position:
                if code[index] == letter:
                    hint += "x"
                # CORRECT number in INCORRECT position:                    
                elif letter in code:
                    hint += "o"
                # INCORRECT number
                else:
                    hint += "*"

            return hint