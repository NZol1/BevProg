def main():
    natrium = int(input("Nátrium(Na): "))
    klor = int(input("Klor(Cl\u2082): "))
    nacl = 0
    kimaradtNatrium = 0
    kimaradtKlor = 0

    if natrium == klor *2: 
        nacl = klor * 2
    elif natrium  > klor*2:
        nacl = natrium // 2
        kimaradtKlor = (natrium - klor)//2
    else:
        nacl = klor // 2
        kimaradtNatrium = (natrium - klor)//2

    print("Létrejött Nátrium-klorid: {3} Na + {4} Cl\u2082 = {0} NaCl\nFent maradó nátrium: {1}\nFent maradó klor: {2}".format(nacl, kimaradtNatrium, kimaradtKlor,natrium,klor))

if __name__ == "__main__":
    main()