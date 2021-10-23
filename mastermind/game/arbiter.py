class Arbiter():
        """Responsible for taking player's guess, checking againnst the code, returning hint           
        ATTRIBUTES:
            none
        """
        def __init__(self):
            """Constructor for Arbiter() class
            Args:
                self (Arbiter)  : an instance of Arbiter
            RETURNS:
                none
            """ 
            pass

        def check_guess(self, code, guess):
            """Creates hints based on the code and guesses given.
            Args:
                self (Arbiter)  : an instance of Arbiter
                code (INT)      : the secret code
                guess (INT)     : the player's guess
            RETURNS:
                hint (STR)
            """ 
            # convert to string
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

# test code
def main():
    arbiter = Arbiter()

    code = 1234
    guesses = [ [1111, "xooo"],
                [2222, "oxoo"],
                [3333, "ooxo"],
                [4444, "ooox"],
                [5555, "****"],
                [6666, "****"],
                [7777, "****"],
                [8888, "****"],
                [9999, "****"],
                [1234, "xxxx"]  ]
    
    TEST_GUESS = 0
    EXPECTED_RESULT = 1

    for set in guesses:
        result = arbiter.check_guess(code, set[TEST_GUESS])
        assert result == set[EXPECTED_RESULT]
        print(f"{result} vs. {set[EXPECTED_RESULT]} : OK")       

if __name__ == "__main__":
    main()