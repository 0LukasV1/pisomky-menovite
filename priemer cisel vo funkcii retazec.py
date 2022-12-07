#napiste funkciu ktora bude mat 1 vstupny parameter, dana funkcia retazec prejde a vrati priemer vsetkych cislic ktorych tam najde
def veta(text:str)->int:
    pocet=0
    sucet=0
    for i in range(len(text)):
        if text[i].isnumeric():
            pocet+=1
            sucet += int(text[i])
        else:
            print("tento znak nie je číslo")
    výsledok=sucet/pocet
    return výsledok

print(veta("a0415g64h56"))
print(veta("jk44dd5g6b465jsdg58jgsd"))
