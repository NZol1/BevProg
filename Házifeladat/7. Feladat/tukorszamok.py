def defaultnums():
    szam1 = 666
    szam2 = 12521
    szam3 = 75422457
    if str(szam1) == str(szam1)[::-1]:
        print("Az alapértelmezett számok közül a szám {0} tükörszám.".format(szam1))
    else:
        print("Az alapértelmezett számok közül a szám {0} nem tükörszám.".format(szam1))
    if str(szam2) == str(szam2)[::-1]:
        print("Az alapértelmezett számok közül a szám {0} tükörszám.".format(szam2))
    else:
        print("Az alapértelmezett számok közül a szám {0} nem tükörszám.".format(szam2))
    if str(szam3) == str(szam3)[::-1]:
        print("Az alapértelmezett számok közül a szám {0} tükörszám.".format(szam3))
    else:
        print("Az alapértelmezett számok közül a szám {0} nem tükörszám.".format(szam3))

def main():
    defaultnums()
    
    proba = 0
    while proba != 3:
        szam = int(input("Kérlek add meg a számot(3 próba áll lehetőségre): "))
        proba += 1
        if str(szam) == str(szam)[::-1]:
            print("Az eredmény igaz! Tehát a szám ugyan az visszafele is.\nA szám: {0}, megfordítva {1}".format(szam,str(szam)[::-1]))
        else:
            print("Az eredmény hamis! Tehát a szám nem ugyan az visszafele.\nA szám: {0}, ha megfordítjuk {1}".format(szam,str(szam)[::-1]))
        
if __name__ == "__main__":
    main()
