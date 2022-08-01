import random
delka = "-" * 50
def randon_cislo():

    tajne_cislo=random.sample("123456789",4)
    tajne_cislo="".join(tajne_cislo)
    return tajne_cislo

def uzivatel_input():
    while(True):
        try:
            global uzivatelske_cislo
            z=uzivatelske_cislo=input("Zadejte sve cislo: ")
            z=int(z)
            if(len(uzivatelske_cislo)!=4):
                print(delka)
                print("Zadejte 4 mistna cisla")
                print(delka)
                continue
            if(uzivatelske_cislo[0]=="0"):
                print(delka)
                print("Prosim, ctyrmistny udaj nesmi zacinat cislem 0")
                print(delka)
                continue
        except ValueError:
            print(delka)
            print("Prosim, zadany vstup neni cislo")
            print(delka)
        else:
            x=0
            for i in range(0,4):
                x=x+uzivatelske_cislo.count(uzivatelske_cislo[i])
            if(x!=4):
                print(delka)
                print("Prosim, zadejte cislo s ruznymi cislicemi")
                print(delka)
                continue
            else:
                return

def hodnotit(a,b):
    a=str(a)
    b=str(b)
    for i in range(0,4):
        for ch in range(0,4):
            if(i==ch)and(a[i]==b[ch]):
                global bull_pocet
                bull_pocet+=1
            elif(i!=ch)and(a[i]==b[ch]):
                global cow_pocet
                cow_pocet+=1
            else:
                pass

print("Dobry den! ")
print(delka)
print("Vygeneroval jsem pro vás náhodné čtyřmístné číslo. ")
print("Zahrajme si hru bulls a cows. ")
print(delka)
uzivatelske_cislo=0
delka2="-"*53
uzivatelska_volba=True
while(uzivatelska_volba):
    cow_pocet=0
    bull_pocet=0
    cislo_hry=randon_cislo()
    pocitadlo=0
    print(cislo_hry)
    while(True):
        uzivatel_input()
        pocitadlo=pocitadlo+1
        hodnotit(cislo_hry,uzivatelske_cislo)
        if(bull_pocet==4):
            print(delka2)
            print("Gratulujeme, jste vyhral !!!")
            print(delka2)
            quit()
        else:
            print(delka)
            print("Bulls:",bull_pocet,"Cows:",cow_pocet)
            cow_pocet=0
            bull_pocet=0
            print(delka)
