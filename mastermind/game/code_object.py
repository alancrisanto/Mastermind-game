import random

class CodeObject:
    """ The responsibility of this class is to generate and store a secret four-digit code to be guesed by the players
    """
    def __init__(self):
        self.min = 1000
        self.max = 9999
        #self.secret_code = random.randint(self.min, self.max)
        # TESTING
        self.secret_code = 1234
    # to reference secret code outside of this class- use "code.secret_code"

# for testing
def main():
    
    console = Console()

    console.display_output("Creating an instance of Code()")
    code = CodeObject()
    console.display_output("Success.\n")

    console.display_output("Printing code.secret_code")
    console.display_output(f"The code is: {code.secret_code}")

if __name__ == "__main__":
    from console import Console
    main()