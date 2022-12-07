
cena = input("Zadaj cenu s DPH: ")
pocet = input("Zadaj mi počet kusov tovaru: ")
cena=int(cena)
pocet=int(pocet)
celkovaCena = cena * pocet
velkoObchCena=(celkovaCena/120)*100
lenDPH=(celkovaCena-velkoObchCena)

print("Za celkový tovar zaplatíš",celkovaCena,",výška len DPH je",lenDPH,"a cena bez DPH je",velkoObchCena)
