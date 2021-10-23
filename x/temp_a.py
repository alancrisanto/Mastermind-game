class Arbiter():
    # placeholder code written by nephi, to be replaced with Felix's Code
    def __init__(self):
        pass

    def check_guess(self,code,guess):
        """
        """
        str_code = str(code)
        str_guess = str(guess)

        if len(str_code) != len(str_guess):
            print("ERROR! STRING LENGTH DOES NOT MATCH!")
        else:
            length = len(str_code)

        # divide each string into characters
        code_chars = []
        for char in str_code:
            code_chars.append(char)

        guess_chars = []
        for char in str_guess:
            guess_chars.append(char)

        hint = ""

        for i in range(length):
            
            # correct number in correct position:
            if str_guess[i] == str_code[i]:
                hint = hint + "x"
            
            # correct number incorrect position
            elif str_guess[i] in code_chars:
                hint = hint + "o"

            else:
                hint = hint + "*"

        #hint = "[[ Arbiter() HINT ]]"
        return hint