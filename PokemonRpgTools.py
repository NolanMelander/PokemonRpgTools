import KantoRouteGenerator as kanto
import TrainerCardCreator as trainer


def pokemonrpgtools():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Pokemon Rpg Tools".center(60, "-"))
    print("Copywrite 2019 | All Rights Reserved".center(60, " "))
    print(version.center(60, " "))

    choice = None
    while choice is not 'q':
        print("\n")
        print("Trainer Card Creator (Currently Unavailable)", "(t)".rjust(22, "."))
        print("Kanto Region (Currently Unavailable)", "(r)".rjust(30, "."))
        print("Quit Pokemon Rpg Tools", "(q)".rjust(20, "."))
        choice = input("\nPlease pick a program to load: ")

        if choice.lower() is 't':
            trainer.trainercardcreator()
        elif choice.lower() is 'r':
            kanto.kantoroutecreator()
        else:
            print("Invalid input. Please try again.")


pokemonrpgtools()