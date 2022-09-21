import random
randnum = random.randint(1,5)
print("Válassz a lehetőségek közül! (A képlet nevének beírásával teheted meg!)\nVálasztási lehetőségek: ( Átlag , Négyzet , Elsőfokú)")
choice = str(input("Választásod: "))

def main(choice):
    if choice == "Átlag" or choice == "Atlag" or choice == "átlag" or choice == "atlag":
        atlagszamlalo = 0
        numbers = []
        print("Kérlek adj meg {0} darab számot: ".format(randnum))
        for x in range(randnum):
            szamok = int(input())
            atlagszamlalo = atlagszamlalo + 1
            #print(atlagszamlalo)
            numbers.append(szamok)
        osszeg = sum(numbers)
        atlagszamit = osszeg / atlagszamlalo
        print("A számaid összege: {0}\nA számaid átlaga: {1}".format(osszeg,atlagszamit))
    elif choice == "Négyzet" or choice == "Negyzet" or choice == "négyzet" or choice == "negyzet":
        negyzetszam = int(input("Kérlek adj meg egy számot amit négyzetre szeretnél emelni: "))
        negyzetli = []
        negyzetli.append(negyzetszam)
        negyzetosszeg = negyzetszam * negyzetszam
        print("A megadott számod {0} négyzete: {1}\nLevezetése: {0}\u00b2 = {0} * {0} = {1}".format(negyzetszam,negyzetosszeg))
    elif choice == "Elsőfokú" or choice == "Elsofoku" or choice == "elsőfokú" or choice == "elsofoku" or choice == "elsőfokú":
        print("Elsőfukú függvény megoldása.")
        randome = random.randint(1,5)
        randomm = random.randint(1,5)
        szamlalo = 0
        while szamlalo < 5:
            unumber = int(input("Adj meg egy számot: "))
            szamlalo += 1
            keplet = unumber * randome + randomm
            kepletosszeg = keplet
            print("f(x) = {0} * {1} + {2}".format(unumber,randome,randomm))
            print("Az x tengelyen {0} -nél/nál az y az {1} lesz\n x = {0} , y = {1}".format(unumber,kepletosszeg))
        
        

if __name__ == "__main__":
    main(choice)
