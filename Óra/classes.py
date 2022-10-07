class BankSzamla:
    def __init__(self,nev,egyenleg) -> None:
        self.dupont = 1000
        self.nev = nev
        self.egyenleg = egyenleg

    def betesz(self,osszeg):
        self.egyenleg += osszeg

    def kivesz(self,osszeg):
        if osszeg > self.egyenleg:
            print("Nincs keretünk erre")
        else:
            self.egyenleg -= osszeg

    def kiiras(self):
        print("Tulaj: {0}\nEgyenleg: {1}".format(self.nev,self.egyenleg))

def main():
    b1 = BankSzamla("Béla",600)
    b1.betesz(1000)
    b1.kivesz(600)
    b1.kiiras()

if __name__ == "__main__":
    main()


