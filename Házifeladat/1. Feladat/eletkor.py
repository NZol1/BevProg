age = int(input("Add meg a korod: "))

def main():
    agedec()

def agedec():
    if age < 12:
        print("Legálisan még nem nézheted meg a Shrek 2. részét!")
    elif age == 12:
        print("Már megnézheted legálisan a Shrek 2. részét!")
    elif age >= 13 and age < 17:
        print("Már megnézheted a Shrek 2. részét, de még nem szerezheted meg a jogosítványodat!")
    elif age == 17:
        print("Már megszerezheted a jogosítványodat!")
    elif age >= 18 and age <= 20:
        print("Magyarországon vehetsz dohányterméket!")
    elif age >= 21:
        print("Legálisan nézheted meg a Shrek 2. részét, vehetsz dohányterméket Magyarországon, szerezheted meg a jogosítványodat, illtve fogyaszthatsz alkoholt Amerikában!")
    

if __name__ == "__main__":
    main()
