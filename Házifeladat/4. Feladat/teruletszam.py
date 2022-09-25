import math


def kor():
    pi = math.pi
    print("Kör területének kiszámításához szükségünk van a sugarának négyzetére azt szoroza TT-vel (PI).")
    global r
    r = int(input("Add meg a kör sugarát: "))
    teruletsz = r ** 2 * pi
    global terulet
    terulet = teruletsz

    print("Kör területe: {0} cm\u00b2 | Kör sugara: {1}\u00b2 * TT (3,14) = {0} cm\u00b2".format(terulet,r,pi))
    
def teglalap():
    print("\nTéglalap területének kiszámításához szükségünk van a téglalap oldalainak hosszára.")
    a = int(input("Add meg a téglalap egyik oldalának hosszát: "))
    b = int(input("Majd add meg a téglalap másik oldalának hosszát: "))
    tegteruletsz = a * b
    global tegterulet
    tegterulet = tegteruletsz
    print("Téglalap területe: {0} cm\u00b2 | Téglalap oldalainak hossza: {1} * {2} = {0} cm\u00b2".format(tegterulet,a,b))
    
def gula():
    print("\nA gúla térfogatának kiszámításához szükségünk van a gúla alapterületére, illetve magasságára.")
    gulaterulet = math.pi * r ** 2
    gulaterfogat = (gulaterulet * tegterulet) / 3
    print("Alapterület: {0} * {1} = {2}\nGúla térfogata: {2} * {3} = {4} cm\u00b3".format(math.pi,r,gulaterulet,tegterulet,gulaterfogat))
    

def main():
    kor()
    teglalap()
    gula()


if __name__ == "__main__":
    main()
