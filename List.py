def main():
    li = ["Alma","Barack","Körte"]
    li2 = []
    li2 = li.copy()
    li.append("Mangó") #Hozzáad a listához (a végéhez)
    li.pop() #Kiszedi a 0. dik elemet (végét, vagy specifikusan megadott sor elemét pl li.pop(0))
    li.sort() #Sorba rendezi a listát
    for x in range(len(li)):
        print(li[x],x)
    
    print(li.index("Körte"))
    print(li2)

if __name__ == "__main__":
    main()