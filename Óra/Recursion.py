def foo(a,b=5,c=4):
    a = a + b-c
    return (a,b)

def rec(a):
    if a < 1:
        return a
    return rec(a-1)

def main():
    print(rec(3))
    # a = 2
    # a = foo(a)
    # print(a)

if __name__ == "__main__":
    main()