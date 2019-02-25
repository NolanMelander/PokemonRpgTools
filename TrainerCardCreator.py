import os
import quantumrandom as qr
import db


def display(tnumber, tname, pokemon):
    print("Trainer Card".center(120, "-"))
    print("Trainer Name: ", tname)
    print("Trainer Number: ", tnumber)
    print("".rjust(30, "-"))
    print("Option 1: ", pokemon[0])
    print("Option 2: ", pokemon[1])
    print("Option 3: ", pokemon[2])
    print("".rjust(30, "-"))

def getpokemon():
    pokemon = ["", "", ""]
    for x in range(3):
        options = db.getstats()
        for rows in options:
            pokemon[x] = (rows[0])
    return pokemon

def registertrainer():
    trainer_name = input("What is the name of the trainer?")

    print("Registering", trainer_name, "...\n")

    trainer_number = int(qr.randint(111111111111, 999999999999))

    print(trainer_name, "registered successfully.")

    return trainer_number, trainer_name


def trainercardcreator():
    version = "VERSION 0.1.0 - ALPHA\n"
    print("Trainer Card Creator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))

    choice = input("Hello there! Would you like to register a new trainer, and enter the world of pokémon (y/n)? ")

    if choice is 'y':
        assert choice is 'y'
        print("Registering new trainer...")
        tnumber, tname = registertrainer()
        print("Checking available pokemon...")
        pokemon = getpokemon()
        print("Pokemon Found.")
        display(tnumber, tname, pokemon)
    elif choice is 'n':
        assert choice is 'n'
        print("Returning to Pokemon Rpg Tools menu...")

    os.system("pause")

