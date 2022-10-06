def decodC():
    decodtext = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    emptyT =""
    for i in range(len(decodtext)):
        decoding = ord(decodtext[i])
        emptyT += chr(decoding - 3)
    print("Az eredeti szöveg: {0}\nDekódolt szöveg: {1}".format(decodtext,emptyT))
    
def main():
    print("Caesar kódolás\n")
    decodC()

if __name__=="__main__":
    main()