import os
import quantumrandom as qr

def routeone():
    pokemon = int(qr.randint(1, 37))
    if 1 <= pokemon <= 3:
       return "Bellsprout"
    elif pokemon == 4 or pokemon == 5:
        return "Furret"
    elif 6 <= pokemon <= 10:
        return "Hoothoot"
    elif pokemon == 11 or pokemon == 12:
        return "Minun"
    elif 13 <= pokemon <= 15:
        return "Oddish"
    elif 16 <= pokemon <= 20:
        return "Pidgey"
    elif pokemon == 21 or pokemon == 22:
        return "Plusle"
    elif 23 <= pokemon <= 26:
        return "Poochyena"
    elif pokemon is 27:
        return "Raticate"
    elif 28 <= pokemon <= 31:
        return "Rattata"
    elif pokemon == 32 or pokemon == 33:
        return "Sentret"
    elif 34 <= pokemon <= 37:
        return "Shinx"
    else:
        return "ERROR"

def getresult(route):
    print("Searching Route please stand by...")

    if route is '1':
        return routeone()
    else:
        return "ERROR"


def kantoroutecreator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Kanto Route Generator".center(60, "-"))
    print("Copyright 2019 | All Rights Reserved".center(60, " "))
    print(version.center(60, " "))


    route = None
    while route is not 'q':
        route = input("Please enter the Kanto route to check, type q to quit: ")
        if route is not 'q':
            result = getresult(route)
            print("A wild ", result, " appeared!")
            os.system("pause")
