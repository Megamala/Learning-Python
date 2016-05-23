#! C:\Python31\python


import re


def main():
    fh = open('raven.txt', encoding="utf8")
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')
    fh = open('raven.txt', encoding="utf8")
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '###', line), end='')


if __name__ == "__main__":
    main()
