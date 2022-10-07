def main():
    #li = [n*2 for n in range(0,10)]
    #print(li)

    #li2 = ["autó","villamos","metró"]
    #li2 = [s.upper()+'!' for s in li2]
    #print(li2)

    text = "1234567"

    li = [i for i in text]
    print(li)
    text2 = "The quick brown fox jumps over the lazy dog"
    li2 = [len(k) for k in text2.split()]
    print(li2)

if __name__ == "__main__":
    main()