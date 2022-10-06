def strvalid():
    print("Feladat -- Bizonyos karakterek")
    valid = "text"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    talalat = ""
    for i in range(len(valid)):
        for y in range(len(chars)):
            if (valid[i] == chars[y]):
                #Itt a string alakítás felesleges volt mert string-ben adtam meg alapból, de biztos ami biztos.
                talalat += str(valid[i])
    print("valid( {0} | {1} ) --> {2} ".format(valid,chars,talalat))
    
def strvalid2():
    print("\nFeladat -- Megoldás #2")
    valid = "textTEXT"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    talalat = ""
    for i in range(len(valid)):
        for y in range(len(chars)):
            if (valid[i] == chars[y]):
                #Itt a string alakítás felesleges volt mert string-ben adtam meg alapból, de biztos ami biztos.
                talalat += str(valid[i])
    print("valid( {0} | {1} ) --> {2} ".format(valid,chars,talalat))
    
def main():
    strvalid()
    strvalid2()

if __name__ == "__main__":
    main()