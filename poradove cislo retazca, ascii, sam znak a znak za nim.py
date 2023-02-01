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




import random
pp = 100

hodnoty={}
for i in range(pp):
    ciki = random.randrange(1,101)
    miki = random.randrange(1,101)
    vysledok = ciki**miki
    cifra = int(str(vysledok)[0])
    hodnoty[cifra] = hodnoty.get(cifra,0)+1
print(hodnoty)

for i in hodnoty:
    print(i, hodnoty[1],(hodnoty[i]/pp)+100)
    
    
    
    import random
monsters= []

def create_monster():
    temp=[]
    for i in range(5):
        temp.append(random.randint(0,10))
    return temp

def iq_test(monster:list)->int:
    return monster.count(1)

def sex(monster1,monster2):
