# napiste funkciu ktora sa bude volat jozo bude mat 1 vstupny parameter a tym bude zoznam, funkcia vrati true ak je v zozname viac parnych ako neparnych cisel
# inak vrati false
def jozo(zoznam: list) -> bool:
    parne = 0
    neparne = 0
    vysledok = False
    if type(zoznam) == list:
        for i in range(0, len(zoznam)):
            if zoznam[i] % 2 == 0:
                parne += 1
            else:
                neparne += 1

        if parne > neparne:
            vysledok = True

        elif parne == neparne:
            vysledok = ("je rovnaký počet párnych a nepárnych čísel")

        return vysledok

    else:
        print("toto nie je zoznam")


print(jozo([3, 3, 7, 7, 5, 8, 2, 2, 2, 2]))
print(jozo([3, 3, 7, 7, 8, 2, 2, 2, 2]))
print(jozo([3, 3, 7, 7, 5, 8, 2, 2, 2]))
