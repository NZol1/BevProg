def main():
    o = open("vers.txt",'r')
    r = o.readlines()
    o.close()
    o2 = open("pielso.txt",'r')
    r2  = o2.readline()
    for i in r2:
        print(i[0])
    o2.close()

if __name__ == "__main__":
    main()