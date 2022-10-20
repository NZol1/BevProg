class Employees():
    def __init__(self,nev,rang,dolgev,fizetes) -> None:
        self.nev = nev
        if dolgev == "" or dolgev == " " or rang == "" or rang == " ":
            self.rang = "Junior"
            self.dolgev = dolgev
        self.fizetes = fizetes
    
    def fizetesem(self,osszeg = 10000):
        self.fizetes += osszeg
        
    def dolgevek(self,evp = 1):
        self.dolgev += evp
        
    def fejlrang(self):
        if self.dolgev == 0:
            self.rang = "Intern"
        elif self.dolgev >= 1 and self.dolgev < 2:
            self.rang = "Junior"
        elif self.dolgev >= 2 and self.dolgev <= 5:
            self.rang = "Medior"
        elif self.dolgev > 5:
            self.rang = "Senior"
        
    def kiir(self):
        print("Név: {0}, Rang: {1}, Dolgév: {2}, Fizetés: {3}".format(self.nev, self.rang,self.dolgev,self.fizetes)) 
        
def main():
    b1 = Employees("Pista","",10,500)
    b1.fizetesem()
    b1.dolgevek()
    b1.fejlrang()
    b1.kiir()
    
    
    
if __name__ == "__main__":
    main()
    