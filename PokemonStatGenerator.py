import os
import db
import quantumrandom as qr


def display():
    pass


def getiv():
    base = [0, 0, 0, 0, 0, 0]
    for x in range(6):
        base[x] = int(qr.randint(0, 35))

    return base


def pokemonstatsgenerator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Pokemon Stat Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))
    print("\n")

    pokemon = pokedex = hp = attack = defense = spa = spd = speed = None

    base = db.getStats()

    for row in base:
        pokemon = (row[0])
        pokedex = (row[1])
        hp = (row[2])
        attack =(row[3])
        defense =(row[4])
        spa =(row[5])
        spd =(row[6])
        speed =(row[7])

    base = getiv()

    os.system("pause")

