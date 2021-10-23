class Console:
    """The responsibility of this class of objects is to:
        * get text or numerical input
        * display text output.
    This class will make it easier to port input or output if the program is
    to be ported to a GUI or Web App, for example.
    Attributes:
        none
    """
    def take_input(self, prompt):
        """Gets text input from the user through the screen.
        Args: 
            self (Console): An instance of Console
            prompt (string): The prompt to display to the user.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def display_output(self, string=""):
        """ Prints text to be read by the user
            Instead of using print() in your functions
            use this method - console.display_output()
        Args:
            self (Console): An instance of Console
            string: the string to be printed, empty by default
        """
        print(string)

# for testing
def main():
    # Create a Console object
    console = Console()

    # Ask a question
    favorite_food = console.take_input("What is your favorite food? ")

    # Display output
    display_string = f"Your favorite food is {favorite_food}!"
    console.display_output(display_string)

if __name__ == "__main__":
    main()