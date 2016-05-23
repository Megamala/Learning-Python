#! C:\Python31\python


import re


def main():
    fh = open('raven.txt', encoding="utf8")
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')


if __name__ == "__main__":
    main()
