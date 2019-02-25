import KantoRouteGenerator as kanto
import TrainerCardCreator as trainer
import PokemonStatGenerator as pokemon

def pokemonrpgtools():
    choice = None
    while choice is not 'q':
        version = "VERSION 0.0.3 - ALPHA\n"
        print("Pokemon Rpg Tools".center(120, "-"))
        print("Copyright 2019 | All Rights Reserved".center(120, " "))
        print(version.center(120, " "))
        print("\n")
        print("Trainer Card Creator (Beta)", "(t)".rjust(22, "."))
        print("Kanto Region (Alpha - Being Reworked)", "(k)".rjust(12, "."))
        print("Pokemon Stat Generator (Beta)", "(p)".rjust(20, "."))
        print("Quit Pokemon Rpg Tools", "(q)".rjust(27, "."))
        choice = input("\nPlease pick a program to load: ")

        if choice is 't':
            assert choice is 't'
            trainer.trainercardcreator()
        elif choice is 'k':
            assert choice is 'k'
            kanto.kantoroutecreator()
        elif choice is 'p':
            pokemon.pokemonstatsgenerator()
        elif choice is not 'q':
            assert choice is not 'q'
            print("Invalid input. Please try again.")


pokemonrpgtools()