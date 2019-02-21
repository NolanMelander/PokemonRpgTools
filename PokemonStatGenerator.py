import os
from math import floor

import db
import quantumrandom as qr


def display(nature, iv, stats, pokemon, pokedex, lvl):
    print("Pokemon: ", pokemon)
    print("National Pokedex: ", pokedex)
    print("Level: ", lvl)
    print("HP: ", stats[0])
    print("POKEMON IV")
    print("HP: ", iv[0])
    print("Attack: ", iv[1])
    print("Defense: ", iv[2])
    print("Spa: ", iv[3])
    print("Spd: ", iv[4])
    print("Speed: ", iv[5])


def gethp(base, iv, ev, lvl):
    hp = floor(((2*base) + iv + floor(ev/4))/100) + lvl + 10
    return hp


def getstats(base, nature, iv, ev):
    pass

def getiv():
    iv = [0, 0, 0, 0, 0, 0]
    for x in range(6):
        iv[x] = int(qr.randint(0, 35))

    return iv


def pokemonstatsgenerator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Pokemon Stat Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))
    print("\n")

    ev = [0, 0, 0, 0, 0, 0]
    lvl = input("Please enter desired pokemon level:")


    print("Generating pokemon. This may take a few minutes. Please wait...")

    base = db.getstats()

    pokemon = None
    pokedex = None
    basestat = [0, 0, 0, 0, 0, 0]
    for row in base:
        pokemon = (row[0])
        pokedex = (row[1])
        basestat[0] = (row[2])
        basestat[1] = (row[3])
        basestat[2] = (row[4])
        basestat[3] = (row[5])
        basestat[4] = (row[6])
        basestat[5] = (row[7])

    nature = db.getnature()

    basenat = [0, 0, 0, 0, 0]
    for row in nature:
        nature = (row[0])
        basenat[0] = (row[2])
        basenat[1] = (row[3])
        basenat[2] = (row[4])
        basenat[3] = (row[5])
        basenat[4] = (row[6])
    iv = getiv()

    stats = [0, 0, 0, 0, 0, 0]

    stats[0] = gethp(basestat[0], iv[0], ev[0], int(lvl))
    display(nature, iv, stats, pokemon, pokedex, lvl)
    os.system("pause")

