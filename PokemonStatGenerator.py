import os

def getstats():
    pokemon = input("Please enter the name of the pokemon: ")
    lvl = input("Please enter the level of the pokemon: ")
    hp = input("Please enter base hp stat for " + pokemon + ": ")
    at = input("Please enter base attack stat for " + pokemon + ": ")
    deff = input("Please enter base defense stat for " + pokemon + ": ")
    spa = input("Please enter base special attack stat for " + pokemon + ": ")
    spd = input("Please enter base special defense stat for " + pokemon + ": ")
    spe = input("Please enter base special defense stat for " + pokemon + ": ")

    return pokemon, lvl, hp, at, deff, spa, spd

def pokemonstatsgenerator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Pokemon Stat Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))
    print("\n")

    pokemon = lvl = hp = at = deff = spa = spd = spe = getstats()


    print(pokemon, lvl, hp, at, deff, spa, spd)

    os.system("pause")