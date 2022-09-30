def main():
    print("Adja meg a téglalap oldalainak méretét: ")
    a = int(input("a oldal: "))
    b = int(input("b oldal: "))
    t = a * b
    k = 2 * (a + b)
    print("A kiszámított terület: ",t)
    print("A kiszámított kerület: ",k)


if __name__ == "__main__":
    main()