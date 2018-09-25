import sys
import Meme_UI


def choose():
    inputs = Meme_UI.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        best_game_ever.start_module()
    elif option == "2":
        nine_gag.start_module()
    elif option == "3":
        hymn.start_module()
    elif option == "4":
        virus.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Best Game Ever",
               "9gag dank memes",
               "Russian Hymn",
               "Virus"]

    Meme_UI.print_menu("Meme menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            Meme_UI.print_error_message(str(err))


if __name__ == '__main__':
    main()