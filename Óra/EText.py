def main():
    c1 = """Totya is a hideous duck. His nose is enourmous , his wings look terrible and he
            doesn't have any feather on his head. Even that Totya is always immaculate since
            he spends most of his time in water. It doesn't matter if his bath is freezing or
            boiling he takes a shower every day!"""

    li = list(c1.split())
    myDict ={
        "hideous" : "very ugly",
        "enourmous" : "very big",
        "immaculate" : "perfect"
    }
    ##for x in myDict:
        ##print(myDict[x])
    #if "hideous" and "enourmous" and "immaculate" in myDict:
        #csere = c1.replace("hideous","very ugly").replace("enourmous","very big").replace("immaculate","perfect")
    #print(csere)

    for word in li:
        if word in myDict:
            print(myDict[word],end=" ")
        else:
            print(word,end =" ")


if __name__ == '__main__':
    main()