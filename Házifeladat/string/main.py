def main():
    fcleanl = []
    rfile = "string1"
    cfile = "string_clean"
    with open(f'{rfile}.txt','r',encoding="utf-8") as rawstring:
        for i in rawstring:
            if i[0] != "#" and i != "\n" and i[4] != "#":
                fcleanl.append(i)
    rawstring.close()
    with open(f'{cfile}.txt','w',encoding="utf-8") as cleanstring:
        for j in fcleanl:
            cleanstring.write(j)
    cleanstring.close()
    print("{0} Nyers fájl megtisztítva! Eredmény a {1} fájlban.".format(rfile,cfile))

if __name__ == "__main__":
    main()
    