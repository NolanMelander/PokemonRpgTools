import os
import quantumrandom as qr


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


def getavailableroutes():
    print("Available Routes")
    print("Route 1")


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
            while int(route) >= 2:
                route = input("Please enter a valid route: ")
            attempts = input("Please enter how many times you would like to check the indicated route: ")
            while not attempts.isnumeric():
                attempts = input("Please enter a valid number: ")
            assert attempts.isnumeric()
            for x in range(int(attempts)):
                result = getresult(route)
                print("A wild ", result, " appeared!")
            os.system("pause")
