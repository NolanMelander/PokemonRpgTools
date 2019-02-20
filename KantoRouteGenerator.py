import os
import quantumrandom as qr


def routefive():
    pokemon = int(qr.randint(1, 438))
    if 1 <= pokemon <= 11:
        return "Abra"
    elif 12 <= pokemon <= 39:
        return "Bellsprout"
    elif 40 <= pokemon <= 49:
        return "Gloom"
    elif 50 <= pokemon <= 79:
        return "Granbull"
    elif 80 <= pokemon <= 99:
        return "Growlithe"
    elif 100 <= pokemon <= 129:
        return "Hoothoot"
    elif 130 <= pokemon <= 138:
        return "Jigglypuff"
    elif 139 <= pokemon <= 163:
        return "Mankey"
    elif 164 <= pokemon <= 189:
        return "Meowth"
    elif 190 <= pokemon <= 209:
        return "Minun"
    elif 210 <= pokemon <= 229:
        return "Noctowl"
    elif 230 <= pokemon <= 270:
        return "Oddish"
    elif 271 <= pokemon <= 283:
        return "Pidgeotto"
    elif 284 <= pokemon <= 324:
        return "Pidgey"
    elif 325 <= pokemon <= 345:
        return "Plusle"
    elif 346 <= pokemon <= 356:
        return "Psyduck"
    elif 357 <= pokemon <= 378:
        return "Rattata"
    elif 379 <= pokemon <= 418:
        return "Shinx"
    elif 419 <= pokemon <= 438:
        return "Vulpix"
    else:
        return "ERROR"


def routefour():
    pokemon = int(qr.randint(1, 632))
    if 1 <= pokemon <= 5:
        return "Arbok"
    elif 6 <= pokemon <= 25:
        return "Bidoof"
    elif 26 <= pokemon <= 45:
        return "Buizel"
    elif 46 <= pokemon <= 50:
        return "Clefairy"
    elif 51 <= pokemon <= 71:
        return "Ekans"
    elif 72 <= pokemon <= 161:
        return "Goldeen"
    elif 162 <= pokemon <= 176:
        return "Gyarados"
    elif 177 <= pokemon <= 231:
        return "Horsea"
    elif 232 <= pokemon <= 241:
        return "Jigglypuff"
    elif 242 <= pokemon <= 296:
        return "Krabby"
    elif 297 <= pokemon <= 316:
        return "Linoone"
    elif 317 <= pokemon <= 371:
        return "Magikarp"
    elif 372 <= pokemon <= 382:
        return "Mankey"
    elif 383 <= pokemon <= 386:
        return "Psyduck"
    elif 387 <= pokemon <= 399:
        return "Raticate"
    elif 400 <= pokemon <= 435:
        return "Rattata"
    elif 436 <= pokemon <= 452:
        return "Sandshrew"
    elif 453 <= pokemon <= 462:
        return "Seaking"
    elif 463 == pokemon:
        return "Slowpoke"
    elif 464 <= pokemon <= 503:
        return "Spearow"
    elif 504 <= pokemon <= 576:
        return "Tentacool"
    elif 577 <= pokemon <= 586:
        return "Tentacruel"
    elif 587 <= pokemon <= 606:
        return "Whismur"
    elif 607 <= pokemon <= 632:
        return "Zubat"
    else:
        return "ERROR"


def routethree():
    pokemon = int(qr.randint(1, 411))
    if 1 <= pokemon <= 5:
        return "Arbok"
    elif 6 <= pokemon <= 45:
        return "Baltoy"
    elif 46 <= pokemon <= 50:
        return "Clefairy"
    elif 51 <= pokemon <= 70:
        return "Ekans"
    elif 71 <= pokemon <=110:
        return "Gulpin"
    elif 111 <= pokemon <= 120:
        return "Jigglypuff"
    elif 121 <= pokemon <= 134:
        return "Mankey"
    elif 135 <= pokemon <= 154:
        return "Minun"
    elif 155 <= pokemon <= 162:
        return "Nidoran (F)"
    elif 163 <= pokemon <= 182:
        return "Nidoran (M)"
    elif 183 <= pokemon <= 224:
        return "Pidgey"
    elif 225 <= pokemon <= 244:
        return "Plusle"
    elif 245 <= pokemon <= 257:
        return "Raticate"
    elif 258 <= pokemon <= 294:
        return "Rattata"
    elif 295 <= pokemon <= 305:
        return "Sandshrew"
    elif 306 <= pokemon <= 345:
        return "Shinx"
    elif 346 <= pokemon <= 385:
        return "Spearow"
    elif 386 <= pokemon <= 411:
        return "Zubat"
    else:
        return "ERROR"


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
    elif route is '3':
        return routethree()
    elif route is '4':
        return routefour()
    elif route is '5':
        return routefive()
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
            assert attempts.isnumeric()
            for x in range(int(attempts)):
                result = getresult(route)
                print("A wild ", result, " appeared!")
            os.system("pause")
