def rec(b):
    res = 1
    for y in b:
        res = res * y
    return res

def main():
    b = [1,2,3,4,5,6]
    print(rec(b))

if __name__ == "__main__":
    main()