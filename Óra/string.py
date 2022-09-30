def both_ends(stri):
    if (len(stri) < 2):
        return ""

    return (stri[0:2] + stri[-2:])

def main():
    txt = "Hello World!"
    print(len(txt))
    print(txt[3])
    print(txt[1:8])
    #Nagy minden
    print(txt.upper())
    #Kicsi minden
    print(txt.lower())
    #Első betűt nagy betűvé alakítja
    print(txt.capitalize())
    #Space utáni első karaktereket nagy betűvé alakítja
    print(txt.title())
    #WildSpace karaktereket törli ki
    print("               hehe          ".strip())
    print(txt.replace("Hello","Henlo"))
    print("Hel;l;o;W;o;rld".split(sep=";"))
    print(txt.find("W"))

    print(both_ends("Spring"))

if __name__ == "__main__":
    main()