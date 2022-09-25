import random
def main():
    fibonacci = int(input("Add meg milyen hosszúságú legyen a sorozat: "))
    if fibonacci == 0:
        print("Mivel 0-át adtál meg ezért a sorozatod automatikusan egy random generált szám lett.")
        fibonacci = random.randint(1,20)
        print("Ez a szám a {0} lett".format(fibonacci))
    elso = 0
    masodik = 1
    i = 0
    while i < fibonacci:
        fib = elso + masodik
        elso = masodik
        masodik = fib
        i += 1
        print(fib)



if __name__ == "__main__":
    main()