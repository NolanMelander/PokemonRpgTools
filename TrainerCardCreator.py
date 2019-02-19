import os
import quantumrandom as qr


def registertrainer():
    trainer_name = input("What is the name of the trainer?")

    print("Registering", trainer_name, "...\n")

    trainer_number = int(qr.randint(111111111111, 999999999999))

    print(trainer_name, "registered successfully.")
    print("Trainer Number: ", trainer_number)
    pass


def trainercardcreator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Trainer Card Creator".center(60, "-"))
    print("Copyright 2019 | All Rights Reserved".center(60, " "))
    print(version.center(60, " "))

    choice = input("Hello there! Would you like to register a new trainer, and enter the world of pokémon (y/n)? ")

    if choice is 'y':
        assert choice is 'y'
        print("Registering new trainer...")
        registertrainer()
    elif choice is 'n':
        assert choice is 'n'
        print("Returning to Pokemon Rpg Tools menu...")

    os.system("pause")
