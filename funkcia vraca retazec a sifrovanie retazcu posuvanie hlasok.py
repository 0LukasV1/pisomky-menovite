#napiste funkciu ktorej vztupnym parametrom je retazec a f bude vracat retazec a vystupny retazec bude ten povodny zasifrovany takym sposobom ze
#samohlasku posunie o 2 a spoluhlasku o 3 doprava, vsetky

def sifra(text: str) -> str:
    samohlaska = "aeiyou"
    x = 0
    a = 0
    b = ""
    for i in range(0, len(text)):
        if text[i] in samohlaska:
            x = ord(text[i])
            a = (((x-97)+2) % 26)+97
            b += chr(a)

        else:
            x = ord(text[i])
            a = (((x-97)+3) % 26)+97
            b += chr(a)
    return b

print(sifra("fungujez"))
