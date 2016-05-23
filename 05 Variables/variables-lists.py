#! C:\Python31\python


def main():
    x = 'string'
    print(type(x), x[2:4])
    # 2:4 is called a slice and gives a slice of the string
    # does not return the last of the slice so only ri not n

    y = (1, 2, 3, 4, 5)
    for i in y:
        print(i)

if __name__ == "__main__":
    main()
