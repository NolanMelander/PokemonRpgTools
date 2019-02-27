import os
from math import floor

import db
import quantumrandom as qr


def display(nature, iv, stats, pokemon, pokedex, lvl):
    print("Pokemon: ", pokemon)
    print("National Pokedex: ", pokedex)
    print("Nature: ", nature)
    print("Level: ", lvl)
    print("POKEMON STATS")
    print("HP: ", stats[0])
    print("ATTACK: ", stats[1])
    print("DEFENSE: ", stats[2])
    print("SPA: ", stats[3])
    print("SPD: ", stats[4])
    print("Speed: ", stats[5])
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


def getstats(base, nature, iv, ev, lvl):
    stat = floor((floor((((2 * base) + iv + floor(ev/4))*lvl)/100)+5)*nature)
    return stat


def getiv():
    iv = [0, 0, 0, 0, 0, 0]
    for x in range(6):
        iv[x] = int(qr.randint(0, 35))

    return iv


def pokemonstatsgenerator():
    version = "VERSION 0.1.0 - BETA\n"
    print("Pokemon Stat Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))
    print("\n")

    choice = None
    natdex = None
    choice = input("Do you wish to generate a specific pokemon (y/n)? ")

    if choice is 'y':
        natdex = input("Please input the National Pokedex number of Pokemon: ")
        choice = input("Do you wish to input iv values? (y/n)")
    else:
        choice = None

    if choice is 'y':
        iv = [0, 0, 0, 0, 0, 0]
        iv[0] = input("Please input the iv value of hp: ")
        iv[1] = input("Please input the iv value of attack: ")
        iv[2] = input("Please input the iv value of defense: ")
        iv[3] = input("Please input the iv value of spa: ")
        iv[4] = input("Please input the iv value of spd: ")
        iv[5] = input("Please input the iv value of speed: ")

    else:
        iv = getiv()

    ev = [0, 0, 0, 0, 0, 0]
    lvl = input("Please enter desired pokemon level: ")

    print("Generating pokemon. This may take a few minutes. Please wait...")

    if choice is None:
        assert(choice is None)
        base = db.getstats()
    else:
        base = db.getstats(int(natdex))

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
    nat = None
    for row in nature:
        nat = (row[0])
        basenat[0] = (row[2])
        basenat[1] = (row[3])
        basenat[2] = (row[4])
        basenat[3] = (row[5])
        basenat[4] = (row[6])

    stats = [0, 0, 0, 0, 0, 0]
    stats[0] = gethp(basestat[0], int(iv[0]), ev[0], int(lvl))
    stats[1] = getstats(basestat[1], basenat[0], int(iv[1]), ev[1], int(lvl))
    stats[2] = getstats(basestat[2], basenat[1], int(iv[2]), ev[2], int(lvl))
    stats[3] = getstats(basestat[3], basenat[2], int(iv[3]), ev[3], int(lvl))
    stats[4] = getstats(basestat[4], basenat[3], int(iv[4]), ev[4], int(lvl))
    stats[5] = getstats(basestat[5], basenat[4], int(iv[5]), ev[5], int(lvl))

    display(nat, iv, stats, pokemon, pokedex, int(lvl))
    os.system("pause")

