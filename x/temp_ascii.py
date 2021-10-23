class AsciiArt:
    """Responsible for displaying ASCII art and user-friendly messages."""
    
    def __init__(self) -> None:
        pass

    def good_job(self):
        #to be used when the guess is correct
        print("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ \n You got it, great job! \n")

    def whoops(self):
        #to be used when the guess contains no right numbers
        print("¯\_(ツ)_/¯ \n Don't give up! \n")

    def game_over(self):
        #for the end of game message
        print("┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ \n"
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
            "\n")


# for testing
def main():
    # Create a AsciiArt object
    art = AsciiArt()
    art.good_job()
    art.whoops()
    art.game_over()


if __name__ == "__main__":
    main()
