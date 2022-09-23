def main():
    li = [1,2,3,4,5,6]
    li2 = [2,3,4,7,8,9]

    for i in li:
        for j in li2:
            if i == j:
                print(i)


if __name__ == '__main__':
    main()