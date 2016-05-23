#! C:\Python31\python


def main():
    a, b = 1, 1
    if a < b:
        v = 'This is true'
    else:
        v = 'This is not true'
    print(v)
    v = 'this is true' if a < b else 'this is not true'
    print(v)

if __name__ == "__main__":
    main()
