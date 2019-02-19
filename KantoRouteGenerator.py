import os
import quantumrandom as qr


def routetwo():
    pokemon = int(qr.randint(1, 451))
    if 1 <= pokemon <= 5:
        return "Ariados"
    elif 6 <= pokemon <= 13:
        return "Beedrill"
    elif 14 <= pokemon <= 33:
        return "Bellsprout"
    elif 34 <= pokemon <= 43:
        return "Butterfree"
    elif 44 <= pokemon <= 65:
        return "Caterpie"
    elif 66 <= pokemon <= 122:
        return "Hoothoot"
    elif 123 <= pokemon <= 139:
        return "Kakuna"
    elif 140 <= pokemon <= 146:
        return "Ledian"
    elif 147 <= pokemon <= 167:
        return "Ledyba"
    elif 168 <= pokemon <= 187:
        return "Metapod"
    elif 188 <= pokemon <= 207:
        return "Minun"
    elif 208 <= pokemon <= 222:
        return "Nidoran (F)"
    elif 233 <= pokemon <= 237:
        return "Nidoran (M)"
    elif 238 <= pokemon <= 250:
        return "Noctowl"
    elif 251 <= pokemon <= 270:
        return "Oddish"
    elif 271 <= pokemon <= 276:
        return "Pidgeotto"
    elif 277 <= pokemon <= 312:
        return "Pidgey"
    elif 313 <= pokemon <= 317:
        return "Pikachu"
    elif 318 <= pokemon <= 337:
        return "Plusle"
    elif 338 <= pokemon <= 372:
        return "Rattata"
    elif 373 <= pokemon <= 412:
        return "Shinx"
    elif 413 <= pokemon <= 434:
        return "Spinarak"
    elif 435 <= pokemon <= 451:
        return "Weedle"
    else:
        return "ERROR"


def routeone():
    pokemon = int(qr.randint(1, 350))
    if 1 <= pokemon <= 30:
       return "Bellsprout"
    elif 31 <= pokemon <= 43:
        return "Furret"
    elif 44 <= pokemon <= 88:
        return "Hoothoot"
    elif 89 <= pokemon <= 108:
        return "Minun"
    elif 109 <= pokemon <= 138:
        return "Oddish"
    elif 139 <= pokemon <= 186:
        return "Pidgey"
    elif 187 <= pokemon <= 206:
        return "Plusle"
    elif 207 <= pokemon <= 246:
        return "Poochyena"
    elif 247 <= pokemon <= 251:
        return "Raticate"
    elif 252 <= pokemon <= 290:
        return "Rattata"
    elif 291 <= pokemon <= 310:
        return "Sentret"
    elif 311 <= pokemon <= 350:
        return "Shinx"
    else:
        return "ERROR"

def getresult(route):
    print("Searching Route please stand by...")

    if route is '1':
        return routeone()
    elif route is '2':
        return routetwo()
    else:
        return "ERROR"


def kantoroutecreator():
    version = "VERSION 0.0.1 - ALPHA\n"
    print("Kanto Route Generator".center(120, "-"))
    print("Copyright 2019 | All Rights Reserved".center(120, " "))
    print(version.center(120, " "))


    route = None
    while route is not 'q':
        route = input("Please enter the Kanto route to check, type q to quit: ")
        if route is not 'q':
            attempts = input("Please enter how many times you would like to check the indicated route: ")
            for x in range(int(attempts)):
                result = getresult(route)
                print("A wild ", result, " appeared!")
            os.system("pause")
