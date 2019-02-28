import os
import quantumrandom as qr

def routethree():
    pokemon = qr.randint(0, 100)
    if 0 <= pokemon <= 5.51:
        return "Pineco"
    elif 5.52 <= pokemon <= 12.86:
        return "Shinx"
    elif 12.87 <= pokemon <= 14.70:
        return "Jigglypuff"
    elif 14.71 <= pokemon <= 18.38:
        return "Minun"
    elif 18.39 <= pokemon <= 26.19:
        return "Spearow"
    elif 26.20 <= pokemon <= 29.87:
        return "Plusle"
    elif 29.88 <= pokemon <= 32.63:
        return "Mankey"
    elif 32.64 <= pokemon <= 39.52:
        return "Rattata"
    elif 39.53 <= pokemon <= 48.71:
        return "Hoothoot"
    elif 48.72 <= pokemon <= 56.06:
        return "Fearow"
    elif 56.07 <= pokemon <= 59.74:
        return "Ekans"
    elif 59.75 <= pokemon <= 67.09:
        return "Baltoy"
    elif 68.01 <= pokemon <= 68.02:
        return "Arbok"
    elif 68.03 <= pokemon <= 70.47:
        return "Raticate"
    elif 70.48 <= pokemon <= 71.38:
        return "Clefairy"
    elif 71.39 <= pokemon <= 72.76:
        return "Nidoran M"
    elif 72.77 <= pokemon <= 74.14:
        return "Nidoran F"
    elif 74.15 <= pokemon <= 81.49:
        return "Gulpin"
    elif 81.50 <= pokemon <= 85.78:
        return "Zubat"
    elif 85.79 <= pokemon <= 93.13:
        return "Pidgey"
    elif 93.14 <= pokemon <= 96.81:
        return "Wurmple"
    elif 96.82 <= pokemon <= 100:
        return "Sandshrew"

def routetwo():
    pokemon = qr.randint(0, 100)
    if 0 <= pokemon <= 7.92:
        return "Shinx"
    elif 7.93 <= pokemon <= 11.88:
        return "Plusle"
    elif 11.89 <= pokemon <= 13.86:
        return "Butterfree"
    elif 13.87 <= pokemon <= 17.82:
        return "Bellsprout"
    elif 17.83 <= pokemon <= 18.81:
        return "Ariados"
    elif 18.82 <= pokemon <= 21.03:
        return "Pidgeotto"
    elif 21.04 <= pokemon <= 32.17:
        return "Hoothoot"
    elif 32.18 <= pokemon <= 33.69:
        return "Ledian"
    elif 33.70 <= pokemon <= 39.76:
        return "Pidgey"
    elif 39.77 <= pokemon <= 44.29:
        return "Spinarak"
    elif 44.30 <= pokemon <= 45.28:
        return "Pidgeot"
    elif 45.29 <= pokemon <= 49.92:
        return "Caterpie"
    elif 49.93 <= pokemon <= 53.02:
        return "Kakuna"
    elif 53.03 <= pokemon <= 54.53:
        return "Beedrill"
    elif 54.44 <= pokemon <= 57.20:
        return "Noctowl"
    elif 57.21 <= pokemon <= 58.19:
        return "Pikachu"
    elif 58.20 <= pokemon <= 61.04:
        return "Weedle"
    elif 61.05 <= pokemon <= 65.51:
        return "Ledyba"
    elif 65.52 <= pokemon <= 69.47:
        return "Metapod"
    elif 69.48 <= pokemon <= 73.43:
        return "Oddish"
    elif 73.44 <= pokemon <= 76.40:
        return "Nidoran F"
    elif 76.41 <= pokemon <= 80.36:
        return "Wurmple"
    elif 80.37 <= pokemon <= 86.30:
        return "Pineco"
    elif 86.31 <= pokemon <= 93.04:
        return "Rattata"
    elif 93.05 <= pokemon <= 96.01:
        return "Nidoran M"
    elif 99.97 <= pokemon <= 100:
        return "Minun"


def routeone():
    pokemon = qr.randint(0, 100)
    if 0 <= pokemon <= 0.99:
        return "Furret"
    elif 1 <= pokemon <= 8.91:
        return "Shinx"
    elif 8.92 <= pokemon <= 14.85:
        return "Ledyba"
    elif 14.86 <= pokemon <= 22.77:
        return "Poochyena"
    elif 22.78 <= pokemon <= 26.73:
        return "Wurmple"
    elif 26.74 <= pokemon <= 33.66:
        return "Pidgeotto"
    elif 33.67 <= pokemon <= 39.60:
        return "Oddish"
    elif 39.61 <= pokemon <= 50.49:
        return "Hoothoot"
    elif 50.50 <= pokemon <= 51.48:
        return "Pidgeot"
    elif 51.49 <= pokemon <= 55.44:
        return "Plusle"
    elif 55.45 <= pokemon <= 56.43:
        return "Raticate"
    elif 56.44 <= pokemon <= 62.37:
        return "Bellsprout"
    elif 62.38 <= pokemon <= 66.33:
        return "Minun"
    elif 66.34 <= pokemon <= 74.16:
        return "Rattata"
    elif 74.17 <= pokemon <= 78.12:
        return "Sentret"
    elif 78.13 <= pokemon <= 84.06:
        return "Spinarak"
    elif 84.07 <= pokemon <= 90:
        return "Pineco"
    elif 91 <= pokemon <= 100:
        return "Pidgey"


def getresult(route):
    print("Searching Route please stand by...")

    if route is '1':
        return routeone()
    elif route is '2':
        return routetwo()
    elif route is '3':
        return routethree()


def getavailableroutes():
    print("Available Routes")
    print("Route 1")
    print("Route 2")
    print("Route 3")


def kantoroutecreator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Kanto Route Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))

    route = None
    while route is not 'q':
        route = input("Please enter the Kanto route to check, type q to quit or r for a list of available routes: ")

        if route is 'r':
            getavailableroutes()
        elif route is not 'q':
            while int(route) >= 4:
                route = input("Please enter a valid route: ")
            attempts = input("Please enter how many times you would like to check the indicated route: ")
            while not attempts.isnumeric():
                attempts = input("Please enter a valid number: ")
            assert attempts.isnumeric()
            for x in range(int(attempts)):
                result = getresult(route)
                print("A wild ", result, " appeared!")
            os.system("pause")
