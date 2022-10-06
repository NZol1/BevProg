def decnumbers():
    number = int(input("Adj meg egy számot: "))
    dnumber = 0
    dwith = 2
    counter = 1
    while counter != 0:
        dnumber = number // dwith
        number = dnumber
        if dnumber <= 1 and dnumber >= 0:
            counter = counter - 1
        print(dnumber%dwith,end="")
def main():
    decnumbers()

if __name__ == "__main__":
    main()