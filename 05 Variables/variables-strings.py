#! C:\Python31\python


def main():
    n = 42
    s = r"This is a {} string!".format(n)
    print(s)
    f = '''\
    this is a string
    line after line
    of text and more
    text.'''
    print(f)

if __name__ == "__main__":
    main()
