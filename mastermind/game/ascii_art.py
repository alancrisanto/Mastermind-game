from game.console import Console

class AsciiArt:
    """Responsible for displaying ASCII art and user-friendly messages.
    ATTRIBUTES:
        console (Console)   : an instance of Console()
    """
    def __init__(self) -> None:        
        self.console = Console()

    def title_screen(self):
        """
        """
        lines = [   "___  ___  ___   _____ _____ ______________  ________ _   _______ ",
                    "|  \/  | / _ \ /  ___|_   _|  ___| ___ \  \/  |_   _| \ | |  _  \\",
                    "| .  . |/ /_\ \\\ `--.  | | | |__ | |_/ / .  . | | | |  \| | | | |",
                    "| |\/| ||  _  | `--. \ | | |  __||    /| |\/| | | | | . ` | | | |",
                    "| |  | || | | |/\__/ / | | | |___| |\ \| |  | |_| |_| |\  | |/ / ",
                    "\_|  |_/\_| |_/\____/  \_/ \____/\_| \_\_|  |_/\___/\_| \_/___/  ",
                    "="*65, ]
        for line in lines:
            self.console.display_output(line)

    def good_job(self):
        """ Prints an encouraging message
            to be used when the guess contains correct numbers
        ARGS:
            self (AsciiArt) : an instance of AsciiArt()
        """
        self.console.display_output("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Almost there, great job!\n")

    def whoops(self):
        """ Prints an encouraging message
            to be used when the guess contains no right numbers
        ARGS:
            self (AsciiArt) : an instance of AsciiArt()
        """        
        self.console.display_output("¯\_(ツ)_/¯ Awww. Don't give up! \n")

    def you_win(self,player_name):
        """ Prints a "YOU WIN" message
        ARGS:
            self (AsciiArt) : an instance of AsciiArt()
        """        
        lines = [   "                                                  ",
                    " __     ______  _    _  __          _______ _   _ ",
                    " \ \   / / __ \| |  | | \ \        / /_   _| \ | |",
                    "  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |",
                    "   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |",
                    "    | | | |__| | |__| |    \  /\  /   _| |_| |\  |",
                    "    |_|  \____/ \____/      \/  \/   |_____|_| \_|",
                    "                                                  ",
                    "                                                  " ]
        for line in lines:
            self.console.display_output(line)

        lines= [   ("="*50),
                    ('{:1}{:^48}{:1}'.format("|",f"WINNER: {player_name}","|")),
                    ("="*50) ]

        for line in lines:
            self.console.display_output(line)          

                                                  
                                                  


    def game_over(self):
        """ Prints a "GAME OVER" message
        ARGS:
            self (AsciiArt) : an instance of AsciiArt()
        """
        self.console.display_output(
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ \n"
            "███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀ \n"
            "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼ \n"
            "██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀ \n"
            "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼ \n"
            "███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄ \n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ \n"
            "███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼ \n"
            "██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼ \n"
            "██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼ \n"
            "██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼ \n"
            "███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄ \n"
            "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ \n")

    def game_over_one_line(self):
        """ Prints a "GAME OVER" message
        ARGS:
            self (AsciiArt) : an instance of AsciiArt()
        """
        lines = [   "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼",
                    "███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀┼┼┼███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼",
                    "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼",
                    "██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀┼┼┼██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼",
                    "██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼┼┼┼██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼",
                    "███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄┼┼┼███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄",
                    "┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼" ]
        for line in lines:
            self.console.display_output(line)

    def encouragement(self, hint):
        """
        """
        if "o" in hint or "x" in hint:
            self.good_job()

        elif "o" not in hint and "x" not in hint:
            self.whoops()

# for testing
def main():
    # Create a AsciiArt object
    art = AsciiArt()
    art.good_job()
    art.whoops()
    art.game_over()


if __name__ == "__main__":
    main()
