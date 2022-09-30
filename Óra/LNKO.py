def lnko(a,b):
    if (a > b):
        return lnko(a - b,b)
    elif (a < b):
        return lnko(a,b - a)
    return a

    

def main():
    a = int(input("Szám1: "))
    b = int(input("Szám2: "))
    print(lnko(a,b))

if __name__ == "__main__":
    main()