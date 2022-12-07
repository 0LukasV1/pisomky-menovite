# vytvorte alebo napiste funkciu vypis, ktora ma 1 vstupny parameter a to retazec a funkia vypise pre kazdy znak tohto retazca 4 udaje: jeho poradove cislo
# jeho ascii hodnotu, samotny znak a znak ktorý nasleduje za nim

def pismenko(text):
    for i in range(0, len(text)):
        x = ord(text[i])
        print(i,end=", ")
        print(x,end=", ")
        print(text[i],end=", ")
        print(chr(x + 1))


pismenko("DneSkA PisEmE pisoMku")
