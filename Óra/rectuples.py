from tkinter import Y


def rec():
    a = [1,2,3,4,5]
    for i in range(len(a)):
        a.append(i)
    return a

def main():
    numbers = rec()
    print(sum(numbers))

if __name__ == "__main__":
    main()