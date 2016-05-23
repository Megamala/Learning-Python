#! C:\Python31\python


def main():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    print(d)
    for k in sorted(d.keys()):
        print(k, d[k])

    c = dict(
        one = 1, two = 2, three = 3, four = 4, five = "five"
    )
    for k in sorted(c.keys()):
        print(k, c[k])

if __name__ == "__main__":
    main()
