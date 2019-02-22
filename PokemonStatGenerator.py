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
    nat = None
    for row in nature:
        nat = (row[0])
        basenat[0] = (row[2])
        basenat[1] = (row[3])
        basenat[2] = (row[4])
        basenat[3] = (row[5])
        basenat[4] = (row[6])



    iv = getiv()

    stats = [0, 0, 0, 0, 0, 0]
    stats[0] = gethp(basestat[0], iv[0], ev[0], int(lvl))

    stats[1] = getstats(basestat[1], basenat[0], iv[1], ev[1], int(lvl))
    stats[2] = getstats(basestat[2], basenat[1], iv[2], ev[2], int(lvl))
    stats[3] = getstats(basestat[3], basenat[2], iv[3], ev[3], int(lvl))
    stats[4] = getstats(basestat[4], basenat[3], iv[4], ev[4], int(lvl))
    stats[5] = getstats(basestat[5], basenat[4], iv[5], ev[5], int(lvl))

    display(nat, iv, stats, pokemon, pokedex, int(lvl))
    os.system("pause")

